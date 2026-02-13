# PFAG モジュール設計書

## 1. モジュール一覧

- `pdf_renderer`：PDF → 画像変換
- `line_detector`：下線検出
- `checkbox_detector`：チェックボックス検出
- `coordinate_mapper`：座標変換
- `acroform_writer`：AcroForm フィールド生成
- `api_server`：FastAPI エンドポイント
- `agent_adapter`：Agent 連携（別リポジトリ or 別層想定）

---

## 2. pdf_renderer モジュール

**責務：**

- PDF をページ単位で画像化
- DPI・ページ範囲の指定
- 一時ファイル管理

**主な関数：**

- `render_pdf_to_images(pdf_bytes, dpi=300) -> List[Image]`
- `get_pdf_page_size(pdf_bytes) -> List[(width_pt, height_pt)]`

---

## 3. line_detector モジュール

**責務：**

- 画像から水平線を検出
- パラメータに応じたフィルタリング

**主な関数：**

- `detect_lines(image, min_line_width, line_gap_threshold) -> List[BoundingBox]`

**出力：**

- 各ページごとの下線候補（バウンディングボックス）

---

## 4. checkbox_detector モジュール

**責務：**

- 画像から矩形（チェックボックス候補）を検出
- アスペクト比・面積・サイズ制約の適用

**主な関数：**

- `detect_checkboxes(image, aspect_ratio_range, area_threshold) -> List[BoundingBox]`

---

## 5. coordinate_mapper モジュール

**責務：**

- 画像座標 → PDF座標の変換
- ページごとのサイズ・解像度に基づくスケーリング

**主な関数：**

- `map_to_pdf_coords(bbox_img, page_width_pt, page_height_pt, img_width_px, img_height_px) -> BoundingBox`

---

## 6. acroform_writer モジュール

**責務：**

- 検出結果に基づき AcroForm フィールドを生成
- 既存フィールドの保持
- 命名規則の適用

**主な関数：**

- `add_text_fields(pdf_bytes, text_fields) -> bytes`
- `add_checkbox_fields(pdf_bytes, checkbox_fields) -> bytes`
- `generate_field_name(page, type, index) -> str`

---

## 7. api_server モジュール

**責務：**

- FastAPI アプリケーションのエントリポイント
- `POST /v1/formify` の実装
- options の解析とパイプライン呼び出し

**主なエンドポイント：**

- `POST /v1/formify`
  - 入力：`file`, `options`
  - 出力：PDF バイナリ + ヘッダ

---

## 8. モジュール間の依存関係

- `api_server`
  - → `pdf_renderer`
  - → `line_detector`
  - → `checkbox_detector`
  - → `coordinate_mapper`
  - → `acroform_writer`

- `agent_adapter`
  - → `api_server`（HTTP 経由）

---

## 9. エラーハンドリング方針（モジュール単位）

- `pdf_renderer`：壊れたPDF → 専用例外 → API 層で 422 にマッピング
- `line_detector` / `checkbox_detector`：検出0件は例外ではなく空リスト
- `acroform_writer`：書き込み失敗時は 500 相当の例外
- `api_server`：例外種別に応じて 422 / 500 を返却

---

## 10. テスト戦略

- `pdf_renderer`：サンプルPDFでページ数・サイズを検証
- `line_detector`：テスト用画像で検出数を検証
- `checkbox_detector`：矩形パターン画像で検出精度を検証
- `coordinate_mapper`：既知座標との誤差を検証
- `acroform_writer`：生成PDFを Acrobat で確認
- `api_server`：統合テスト（/v1/formify）