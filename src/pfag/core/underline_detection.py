# 下線検出サービス本体（スケルトン）

from typing import List, Tuple, Optional

class UnderlineDetectionService:
        def draw_underlines_on_image(self, image_path: str, underlines: List[dict], color=(0, 0, 255), thickness: int = 2, out_path: str = None) -> str:
            """
            画像に下線を描画し、保存する
            Args:
                image_path (str): 入力画像パス
                underlines (List[dict]): 下線リスト
                color (tuple): 線色（BGR）
                thickness (int): 線の太さ
                out_path (str): 保存先パス（Noneなら一時ファイル）
            Returns:
                str: 保存先パス
            """
            import cv2
            import tempfile
            img = cv2.imread(image_path, cv2.IMREAD_COLOR)
            for u in underlines:
                cv2.line(img, (u["start_x"], u["start_y"]), (u["end_x"], u["end_y"]), color, thickness)
            if out_path is None:
                tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
                out_path = tmp.name
                tmp.close()
            cv2.imwrite(out_path, img)
            return out_path
    def __init__(self):
        pass

    def preprocess_image(self, image_path: str):
        import time
        start = time.time()
        """
        画像をグレースケール化・二値化・ノイズ除去して返す
        Returns: 前処理済み画像（OpenCV形式）
        """
        import cv2
        import numpy as np
        import logging
        img = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if img is None:
            logging.error(f"画像ファイルが見つかりません: {image_path}")
            raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")
        if img.shape[0] > 1200 or img.shape[1] > 1200:
            logging.error(f"画像サイズが大きすぎます: {img.shape}")
            raise ValueError(f"画像サイズが大きすぎます: {img.shape}")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # ノイズ除去（ガウシアンブラー）
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        # 二値化
        _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        elapsed = time.time() - start
        if elapsed > 1.0:
            print(f"[WARN] preprocess_image: {elapsed:.2f}s")
        return binary

    def detect_underlines(self, image_path: str, min_line_width: int = 30, line_gap_threshold: int = 5, min_thickness: int = 2, min_length: int = 50) -> List[dict]:
        import time
        start = time.time()
        """
        画像またはPDFから水平下線を検出する（前処理＋水平線強調まで実装）
        """
        import cv2
        binary = self.preprocess_image(image_path)
        # 水平線強調（モルフォロジー演算）
        horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))
        detected_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
        # Hough変換で直線抽出
        lines = cv2.HoughLinesP(
            detected_lines,
            rho=1,
            theta=np.pi/180,
            threshold=100,
            minLineLength=min_length,
            maxLineGap=line_gap_threshold
        )
        results = []
        seen = set()
        if lines is not None:
            for l in lines:
                x1, y1, x2, y2 = l[0]
                width = abs(x2 - x1)
                thickness_val = abs(y2 - y1)
                # 水平線のみ（角度フィルタ: y差2px以内）
                if thickness_val <= min_thickness and width >= min_line_width:
                    # 最小長さ・画像端付近除外
                    if width < min_length:
                        continue
                    # 重複除去（座標丸め）
                    key = (round(x1, -1), round(y1, -1), round(x2, -1), round(y2, -1))
                    if key in seen:
                        continue
                    seen.add(key)
                    # 画像端から5px以内は除外
                    if min(x1, x2) < 5 or max(x1, x2) > 995:
                        continue
                    results.append({
                        "start_x": int(x1),
                        "start_y": int(y1),
                        "end_x": int(x2),
                        "end_y": int(y2),
                        "width": int(width),
                        "thickness": int(thickness_val)
                    })
        elapsed = time.time() - start
        if elapsed > 2.0:
            print(f"[WARN] detect_underlines: {elapsed:.2f}s ({image_path})")
        return results

    def generate_bounding_boxes(self, underlines: List[dict], height: int = 20, offset: int = 5, inset: int = 2) -> List[dict]:
        """
        下線リストからバウンディングボックスを生成
        Args:
            underlines (List[dict]): 下線リスト
            height (int): ボックス高さ
            offset (int): Y方向オフセット
            inset (int): X方向インセット
        Returns:
            List[dict]: バウンディングボックスリスト
        """
        boxes = []
        for u in underlines:
            x1 = min(u["start_x"], u["end_x"]) + inset
            x2 = max(u["start_x"], u["end_x"]) - inset
            y = min(u["start_y"], u["end_y"]) - offset
            w = max(0, x2 - x1)
            h = height
            boxes.append({
                "x": int(x1),
                "y": int(y),
                "width": int(w),
                "height": int(h)
            })
        return boxes

    def apply_field_layout(self, bounding_boxes: List[dict], layout_rule: Optional[dict] = None) -> List[dict]:
        """
        バウンディングボックスにフィールド配置ルール（高さ・オフセット・インセット）を適用
        Args:
            bounding_boxes (List[dict]): バウンディングボックスリスト
            layout_rule (dict): {"height": int, "offset": int, "inset": int}
        Returns:
            List[dict]: 配置ルール適用済みボックス
        """
        if layout_rule is None:
            layout_rule = {"height": 20, "offset": 5, "inset": 2}
        result = []
        for box in bounding_boxes:
            b = box.copy()
            b["height"] = layout_rule.get("height", 20)
            b["y"] = b["y"] - layout_rule.get("offset", 5)
            b["x"] = b["x"] + layout_rule.get("inset", 2)
            b["width"] = max(0, b["width"] - 2 * layout_rule.get("inset", 2))
            result.append(b)
        return result
