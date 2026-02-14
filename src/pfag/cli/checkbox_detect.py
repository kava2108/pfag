# チェックボックス検出CLIスケルトン



import argparse
from pfag.core.checkbox_detection import CheckboxDetectionService
import sys
import logging

def main():
    parser = argparse.ArgumentParser(description="チェックボックス検出CLI")
    parser.add_argument("image", help="入力画像ファイルパス")
    parser.add_argument("--min-size", type=int, default=15, help="最小サイズ")
    parser.add_argument("--max-size", type=int, default=50, help="最大サイズ")
    parser.add_argument("--fill-threshold", type=float, default=0.5, help="塗りつぶし判定しきい値")
    args = parser.parse_args()

    service = CheckboxDetectionService()
    try:
        checkboxes = service.detect_checkboxes(
            args.image,
            min_size=args.min_size,
            max_size=args.max_size,
            fill_threshold=args.fill_threshold
        )
        json_str = service.to_json(checkboxes)
        print(json_str)
    except Exception as e:
        logging.exception(f"検出処理でエラー: {e}")
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
