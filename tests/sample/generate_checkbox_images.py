import cv2
import numpy as np
import os

def generate_checkbox_image(path, width=200, height=100, box_x=50, box_y=30, box_size=20, fill=False):
    img = np.ones((height, width, 3), dtype=np.uint8) * 255
    color = (0, 0, 0)
    thickness = 2
    cv2.rectangle(img, (box_x, box_y), (box_x+box_size, box_y+box_size), color, thickness)
    if fill:
        cv2.rectangle(img, (box_x+4, box_y+4), (box_x+box_size-4, box_y+box_size-4), color, -1)
    cv2.imwrite(path, img)

def generate_multi_checkbox_image(path):
    img = np.ones((100, 200, 3), dtype=np.uint8) * 255
    color = (0, 0, 0)
    for i in range(3):
        x = 30 + i*50
        y = 30
        cv2.rectangle(img, (x, y), (x+20, y+20), color, 2)
        if i == 1:
            cv2.rectangle(img, (x+4, y+4), (x+16, y+16), color, -1)
    cv2.imwrite(path, img)

def generate_non_rect_image(path):
    img = np.ones((100, 200, 3), dtype=np.uint8) * 255
    pts = np.array([[50,30],[70,30],[75,50],[45,50]], np.int32).reshape((-1,1,2))
    cv2.polylines(img, [pts], isClosed=True, color=(0,0,0), thickness=2)
    cv2.imwrite(path, img)

def generate_noise_image(path):
    img = np.random.randint(0, 256, (100, 200, 3), dtype=np.uint8)
    cv2.imwrite(path, img)

def generate_pdf_from_image(image_path, pdf_path):
    try:
        from PIL import Image
        img = Image.open(image_path)
        img.save(pdf_path, "PDF", resolution=100.0)
    except Exception as e:
        print(f"PDF生成失敗: {e}")

if __name__ == "__main__":
    os.makedirs("tests/sample", exist_ok=True)
    generate_checkbox_image("tests/sample/checkbox_on.png", fill=True)
    generate_checkbox_image("tests/sample/checkbox_off.png", fill=False)
    print("サンプル画像を生成しました: tests/sample/")
