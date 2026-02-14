# チェックボックス検出サービス本体（スケルトン）


class CheckboxDetectionService:
            def generate_preview_image(self, image_path, checkboxes, output_path):
                import cv2
                import numpy as np
                img = cv2.imread(image_path, cv2.IMREAD_COLOR)
                if img is None:
                    raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")
                for box in checkboxes:
                    color = (0, 255, 0) if box["is_checked"] else (0, 0, 255)
                    x, y, w, h = box["x"], box["y"], box["width"], box["height"]
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.imwrite(output_path, img)
        def to_json(self, checkboxes):
            import json
            # バリデーション: 必須キーと型
            for box in checkboxes:
                assert all(k in box for k in ("x", "y", "width", "height", "is_checked")), "Missing key in checkbox dict"
                assert isinstance(box["x"], int)
                assert isinstance(box["y"], int)
                assert isinstance(box["width"], int)
                assert isinstance(box["height"], int)
                assert isinstance(box["is_checked"], bool)
            return json.dumps({"checkboxes": checkboxes}, ensure_ascii=False, indent=2)
    def __init__(self):
        pass

    def preprocess_image(self, image_path: str) -> 'np.ndarray':
        import cv2
        import numpy as np
        import logging
        img = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if img is None:
            logging.error(f"画像ファイルが見つかりません: {image_path}")
            raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")
        try:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (3, 3), 0)
            _, binary = cv2.threshold(blurred, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            return binary
        except Exception as e:
            logging.exception(f"画像前処理でエラー: {e}")
            raise

    def detect_checkboxes(
        self,
        image_path: str,
        min_size: int = 15,
        max_size: int = 50,
        fill_threshold: float = 0.5,
        angle_threshold: float = 10.0
    ) -> list:
        import cv2
        import numpy as np
        binary = self.preprocess_image(image_path)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        checkboxes = []
        for cnt in contours:
            if cv2.contourArea(cnt) < min_size * min_size:
                continue  # 小さすぎるノイズ除外
            epsilon = 0.02 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            if len(approx) == 4 and cv2.isContourConvex(approx):
                x, y, w, h = cv2.boundingRect(approx)
                aspect_ratio = w / float(h)
                # 角度チェック
                def angle(pt1, pt2, pt0):
                    dx1 = pt1[0][0] - pt0[0][0]
                    dy1 = pt1[0][1] - pt0[0][1]
                    dx2 = pt2[0][0] - pt0[0][0]
                    dy2 = pt2[0][1] - pt0[0][1]
                    denom = (np.sqrt(dx1 * dx1 + dy1 * dy1) * np.sqrt(dx2 * dx2 + dy2 * dy2) + 1e-7)
                    if denom == 0:
                        return 0
                    angle = np.arccos(
                        (dx1 * dx2 + dy1 * dy2) / denom
                    )
                    return np.degrees(angle)
                angles = [angle(approx[(i+1)%4], approx[(i-1)%4], approx[i]) for i in range(4)]
                if not all(abs(a - 90) <= angle_threshold for a in angles):
                    continue  # 直角でなければ除外
                if (
                    min_size <= w <= max_size and
                    min_size <= h <= max_size and
                    0.8 <= aspect_ratio <= 1.2
                ):
                    # 塗りつぶし判定: ROI内の黒画素率
                    roi = binary[y+3:y+h-3, x+3:x+w-3] if w > 6 and h > 6 else binary[y:y+h, x:x+w]
                    total_pixels = roi.size
                    if total_pixels == 0:
                        continue
                    black_pixels = np.count_nonzero(roi < 128)
                    fill_ratio = black_pixels / total_pixels
                    is_checked = fill_ratio > fill_threshold
                    checkboxes.append({
                        "x": int(x),
                        "y": int(y),
                        "width": int(w),
                        "height": int(h),
                        "is_checked": bool(is_checked)
                    })
        return checkboxes
