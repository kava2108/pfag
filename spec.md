# PDF Form Auto-Generator (PFAG) — 仕様書（AI-SDD v2.1）

## 1. 課題背景（Problem Statement）

多くの組織では、手書き入力を前提とした「静的PDF（下線や枠線のみ）」が依然として利用されている。  
これらを入力可能なPDFフォームへ変換する作業は手作業で行われ、時間と労力がかかり、人的ミスも発生しやすい。

PFAG は、既存PDF内の入力欄候補（下線・チェックボックス）を自動検出し、AcroForm フィールドを自動配置することで、この問題を解決する。

---

## 2. 目的（Goals）

- 静的PDF内の下線・矩形を自動検出する。
- 検出領域を AcroForm フィールド（`/Tx`, `/Btn`）として自動生成する。
- マルチページPDFに対応する。
- FastAPI による REST API を提供する。
- Agent Skills（Copilot）と連携し、会話ベースのワークフローを実現する。
- 検出結果が再現性・決定性を持つように設計する。

---

## 3. 非対象範囲（Non-Goals）

- OCR によるラベル理解（例：「氏名」→フィールド名）は行わない。
- ラジオボタンのグループ化ロジック。
- 特殊フォントの埋め込みや外字保持。
- PDF レイアウト編集や構造修復。
- 高度な PDF セキュリティ（署名、暗号化など）。

---

## 4. 機能要件（Functional Requirements）

### F-001: PDF解析・フォーム変換エンジン
- PyMuPDF により PDF → 画像（300dpi）へ変換。
- OpenCV による特徴抽出。
- 画像座標 → PDF座標への変換（アスペクト比補正・原点差異の吸収）。
- 既存 AcroForm を保持しつつ、新規フィールドを追加する。

### F-002: 下線（テキストフィールド）検出
- モルフォロジー演算で水平線を強調。
- パラメータ：
  - `min_line_width`: 最小線幅
  - `line_gap_threshold`: 途切れ線の連結許容
- フィールド配置ルール：
  - 高さ：12〜14pt（または `line_height * 3`）
  - 垂直オフセット：線の上 2pt
  - 左右インセット：±2pt

### F-003: 矩形（チェックボックス）検出
- `cv2.findContours` による輪郭抽出。
- 形状フィルタ：
  - アスペクト比：0.8 < W/H < 1.2
  - 面積閾値：ページ面積比で判定
- 最終Rect：
  - 短辺基準で正方形化
  - 中心位置を維持
  - サイズ：8〜20pt

### F-004: フィールド命名規則
- `field_p{page}_{type}{index}`
  - 例：`field_p1_t1`, `field_p1_c1`
- 既存フィールドは削除せず append 方式で追加。

### F-005: 座標変換
- PDF座標：左下原点  
- 画像座標：左上原点  
- 変換式：
  - `X_pdf = X_img * (Width_pdf / Width_img)`
  - `Y_pdf = Height_pdf - (Y_img * (Height_pdf / Height_img))`

---

## 5. 非機能要件（Non-Functional Requirements）

### 5.1 パフォーマンス
- 1ページあたり平均1秒以内。
- 大容量PDFではメモリ使用量を制御。

### 5.2 セキュリティ
- TemporaryDirectory による一時ファイルの即時削除。
- JavaScript 埋め込みPDFは拒否。

### 5.3 信頼性・エラーハンドリング
- 検出0件でも 200 OK + 元PDF を返却。
- `X-PFAG-Warning` ヘッダで警告を通知。
- Agent は警告内容をユーザーに説明する。

---

## 6. API仕様

### POST /v1/formify

#### Request
- `file`: PDF バイナリ
- `options`: JSON
  - `detection_mode`: `"auto" | "text_only" | "checkbox_only"`
  - `sensitivity`: 0.1〜1.0
  - `output_prefix`: フィールド名接頭辞

#### Response
- `200 OK`: 変換後PDF（警告ヘッダあり得る）
- `422`: PDF解析失敗
- `500`: タイムアウト・内部エラー

---

## 7. Agent Skills 連携

### 7.1 会話フロー
1. ユーザー：「このPDFを入力可能にして」
2. Agent：自動検出の確認
3. API 呼び出し
4. 結果PDFの提示
5. 警告があれば説明
6. 必要に応じて再試行（感度調整）

### 7.2 適応動作
- 「線が認識されない」→ `sensitivity` を上げて再試行

---

## 8. 受け入れ基準（Acceptance Criteria）

- 明確な下線・矩形の 90%以上を検出できる。
- 生成PDFが Acrobat で正常に入力可能。
- マルチページで一貫した検出が行われる。
- API が適切なステータスコードと警告を返す。
- Agent が警告を正しく説明できる。