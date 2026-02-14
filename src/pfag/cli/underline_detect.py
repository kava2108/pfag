
# 下線検出CLI
# usage:
#   python -m pfag.cli.underline_detect --file 入力画像.png --output result.json --preview preview.png
#
# 引数:
#   --file: 入力画像またはPDFファイルパス（必須）
#   --min_line_width: 最小下線幅（px, デフォルト30）
#   --line_gap_threshold: 途切れ線連結閾値（px, デフォルト5）
#   --thickness: 最小下線太さ（px, デフォルト2）
#   --min_length: 最小下線長さ（px, デフォルト50）
#   --output: 検出結果（JSON）出力先
#   --preview: 下線付き画像出力先
#
# 出力例:
#   {
#     "underlines": [ {"x1":..., "y1":..., "x2":..., "y2":..., "width":..., "thickness":...}, ... ],
#     "boxes": [ {"x":..., "y":..., "w":..., "h":...}, ... ]
#   }

import argparse
from pfag.core.underline_detection import UnderlineDetectionService
import json
import os

def main():
    parser = argparse.ArgumentParser(description="下線検出CLI: 画像またはPDFから水平下線を検出")
    parser.add_argument('--file', type=str, required=True, help='入力画像またはPDFファイルパス（必須）')
    parser.add_argument('--min_line_width', type=int, default=30, help='最小下線幅（px, デフォルト30）')
    parser.add_argument('--line_gap_threshold', type=int, default=5, help='途切れ線連結閾値（px, デフォルト5）')
    parser.add_argument('--thickness', type=int, default=2, help='最小下線太さ（px, デフォルト2）')
    parser.add_argument('--min_length', type=int, default=50, help='最小下線長さ（px, デフォルト50）')
    parser.add_argument('--output', type=str, help='検出結果（JSON）出力先')
    parser.add_argument('--preview', type=str, help='下線付き画像出力先')
    args = parser.parse_args()

    service = UnderlineDetectionService()
    underlines = service.detect_underlines(
        args.file,
        min_line_width=args.min_line_width,
        line_gap_threshold=args.line_gap_threshold,
        min_thickness=args.thickness,
        min_length=args.min_length
    )
    boxes = service.generate_bounding_boxes(underlines)
    # 結果出力
    result = {"underlines": underlines, "boxes": boxes}
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"検出結果を {args.output} に保存しました")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    # プレビュー画像出力
    if args.preview:
        out_path = service.draw_underlines_on_image(args.file, underlines, out_path=args.preview)
        print(f"下線付き画像を {out_path} に保存しました")

if __name__ == "__main__":
    main()
