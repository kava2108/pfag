import cv2
import numpy as np
import os

def generate_horizontal_line(path, width=200, height=100, line_y=50):
    img = np.ones((height, width, 3), dtype=np.uint8) * 255
    cv2.line(img, (10, line_y), (width-10, line_y), (0,0,0), 2)
    cv2.imwrite(path, img)

def generate_multiple_lines(path, width=200, height=100):
    img = np.ones((height, width, 3), dtype=np.uint8) * 255
    for y in [30, 50, 70]:
        cv2.line(img, (10, y), (width-10, y), (0,0,0), 2)
    cv2.imwrite(path, img)

def generate_noisy_image(path, width=200, height=100):
    img = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    cv2.line(img, (10, 50), (width-10, 50), (0,0,0), 2)
    cv2.imwrite(path, img)

if __name__ == "__main__":
    os.makedirs("tests/sample", exist_ok=True)
    generate_horizontal_line("tests/sample/horizontal.png")
    generate_multiple_lines("tests/sample/multiple.png")
    generate_noisy_image("tests/sample/noisy.png")
    print("サンプル画像を生成しました: tests/sample/")
