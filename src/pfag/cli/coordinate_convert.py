import argparse
from pfag.core.coordinate_conversion import convert_coordinates, CoordinateConversionError

def main():
    parser = argparse.ArgumentParser(description="画像座標→PDF座標変換ツール")
    parser.add_argument("--x", type=int, required=True, help="画像X座標")
    parser.add_argument("--y", type=int, required=True, help="画像Y座標")
    parser.add_argument("--img-width", type=int, required=True, help="画像幅(px)")
    parser.add_argument("--img-height", type=int, required=True, help="画像高さ(px)")
    parser.add_argument("--pdf-width", type=float, required=True, help="PDF幅(pt)")
    parser.add_argument("--pdf-height", type=float, required=True, help="PDF高さ(pt)")
    args = parser.parse_args()
    try:
        # アスペクト比差異チェック
        aspect_img = args.img_width / args.img_height
        aspect_pdf = args.pdf_width / args.pdf_height
        aspect_diff = abs(aspect_img - aspect_pdf)
        if aspect_diff > 0.2:
            print(f"警告: アスペクト比差異が大きい (画像={aspect_img:.2f}, PDF={aspect_pdf:.2f})")
        from pfag.core.coordinate_conversion import calculate_error_margin
        x_pdf, y_pdf = convert_coordinates(
            args.x, args.y, args.img_width, args.img_height, args.pdf_width, args.pdf_height
        )
        error_x, error_y = calculate_error_margin(
            args.x, args.y, args.img_width, args.img_height, args.pdf_width, args.pdf_height
        )
        print(f"PDF座標: ({x_pdf:.2f}, {y_pdf:.2f}) 誤差: X={error_x:.2f}pt, Y={error_y:.2f}pt")
    except CoordinateConversionError as e:
        print(f"エラー: {e}")
        exit(1)

if __name__ == "__main__":
    main()
