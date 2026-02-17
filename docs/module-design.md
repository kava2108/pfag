---

## バージョン情報 / Version Info
- バージョン: 1.0.0
- 最終更新日 / Last updated: 2026-02-17

## 更新履歴 / History
- 2026-02-17: ドキュメント改善（Issue 10）対応、Glossary・英語併記・設計方針明確化
# PFAG モジュール設計書 / PFAG Module Design Document

## 概要 / Overview
このドキュメントはPFAGシステムの主要モジュール構成・責務・設計方針を日本語・英語併記で記載します。
This document describes the main module structure, responsibilities, and design policies of the PFAG system in both Japanese and English.

---

## 表記ゆれ防止ガイドライン / Consistency Guidelines
- ファイル名・モジュール名は英数字・ハイフンのみ / Use only alphanumeric and hyphens for file/module names
- 用語はGlossaryに登録し、docs/・specs/で統一 / Register all terms in the Glossary and use consistently in docs/specs
- 日本語・英語併記を推奨 / Use both Japanese and English where possible
- ファイル名・モジュール名は一意で重複禁止 / File/module names must be unique

---

## 用語集 / Glossary
| 用語 (JP) | Term (EN) | 説明 / Description |
|---|---|---|
| モジュール | Module | システムの機能単位 / Functional unit of the system |
| 責務 | Responsibility | モジュールが担う役割 / Role of the module |
| Glossary | Glossary | 用語集 / List of terms |
| 表記ゆれ | Consistency | 用語・表現の不統一 / Inconsistent terms or expressions |
| 一意性 | Uniqueness | 名前や識別子が重複しないこと / No duplicate names or identifiers |

# Agent Skills連携 概要
# 各モジュールの責務・役割分担 / Responsibilities and Roles of Each Module

各モジュールは以下の責務・役割を持ちます。
Each module has the following responsibilities and roles.

## 機能構成
- Skillスキーマ定義（入力/出力/説明/バージョン）
- Skill呼び出しAPI/CLIラッパ
- 感度調整・警告説明API/CLI

## 主なモジュール
- src/pfag/skills/schema.py: SkillSchemaモデル
- src/pfag/skills/wrapper.py: SkillWrapper（APIラッパ）
- src/pfag/skills/sensitivity.py: SensitivityParam（感度調整）
- src/pfag/skills/warning.py: WarningMessage/警告ロジック
- src/pfag/api/skills.py: FastAPIルーティング
- src/pfag/cli/skills.py: Typer CLI

## テスト
- contract/integration/unitテストで各USを独立検証

## 今後の拡張
- DB保存/外部API連携/スキル自動発見 など
# PFAG モジュール設計書

## 1. モジュール一覧

- `pdf_renderer`：PDF → 画像変換 / Converts PDF to images
- `line_detector`：下線検出 / Detects underlines in images
- `checkbox_detector`：チェックボックス検出 / Detects checkboxes in images
- `coordinate_mapper`：座標変換 / Maps image coordinates to PDF coordinates
- `acroform_writer`：AcroForm フィールド生成 / Generates AcroForm fields
- `api_server`：FastAPI エンドポイント / FastAPI endpoints
- `agent_adapter`：Agent 連携（別リポジトリ or 別層想定）/ Agent integration (external repo or layer)

---


## 2. pdf_renderer モジュール / pdf_renderer Module

**責務 / Responsibility:**
- PDF をページ単位で画像化 / Convert PDF to images per page
- DPI・ページ範囲の指定 / Specify DPI and page range
- 一時ファイル管理 / Manage temporary files

**主な関数 / Main Functions:**
- `render_pdf_to_images(pdf_bytes, dpi=300) -> List[Image]`
- `get_pdf_page_size(pdf_bytes) -> List[(width_pt, height_pt)]`

---


## 3. line_detector モジュール / line_detector Module

**責務 / Responsibility:**
- 画像から水平線を検出 / Detect horizontal lines in images
- パラメータに応じたフィルタリング / Filter by parameters

**主な関数 / Main Functions:**
- `detect_lines(image, min_line_width, line_gap_threshold) -> List[BoundingBox]`

**出力 / Output:**
- 各ページごとの下線候補（バウンディングボックス）/ Underline candidates (bounding boxes) per page

---


## 4. checkbox_detector モジュール / checkbox_detector Module

**責務 / Responsibility:**
- 画像から矩形（チェックボックス候補）を検出 / Detect rectangles (checkbox candidates) in images
- アスペクト比・面積・サイズ制約の適用 / Apply aspect ratio, area, and size constraints

**主な関数 / Main Functions:**
- `detect_checkboxes(image, aspect_ratio_range, area_threshold) -> List[BoundingBox]`

---


## 5. coordinate_mapper モジュール / coordinate_mapper Module

**責務 / Responsibility:**
- 画像座標 → PDF座標の変換 / Convert image coordinates to PDF coordinates
- ページごとのサイズ・解像度に基づくスケーリング / Scale based on page size and resolution

**主な関数 / Main Functions:**
- `map_to_pdf_coords(bbox_img, page_width_pt, page_height_pt, img_width_px, img_height_px) -> BoundingBox`

---


## 6. acroform_writer モジュール / acroform_writer Module

**責務 / Responsibility:**
- 検出結果に基づき AcroForm フィールドを生成 / Generate AcroForm fields based on detection results
- 既存フィールドの保持 / Preserve existing fields
- 命名規則の適用 / Apply naming conventions

**主な関数 / Main Functions:**
- `add_text_fields(pdf_bytes, text_fields) -> bytes`
- `add_checkbox_fields(pdf_bytes, checkbox_fields) -> bytes`
- `generate_field_name(page, type, index) -> str`

---


## 7. api_server モジュール / api_server Module

**責務 / Responsibility:**
- FastAPI アプリケーションのエントリポイント / Entry point for FastAPI application
- `POST /v1/formify` の実装 / Implements `POST /v1/formify`
- options の解析とパイプライン呼び出し / Parse options and call pipeline

**主なエンドポイント / Main Endpoints:**
- `POST /v1/formify`
  - 入力 / Input: `file`, `options`
  - 出力 / Output: PDF バイナリ + ヘッダ / PDF binary + headers

---


## 8. モジュール間の依存関係 / Module Dependencies

- `api_server`
  - → `pdf_renderer`
  - → `line_detector`
  - → `checkbox_detector`
  - → `coordinate_mapper`
  - → `acroform_writer`

- `agent_adapter`
  - → `api_server`（HTTP 経由 / via HTTP）

---


## 9. エラーハンドリング方針（モジュール単位） / Error Handling Policy (per module)

- `pdf_renderer`: 壊れたPDF → 専用例外 → API 層で 422 にマッピング / Broken PDF → custom exception → mapped to 422 in API layer
- `line_detector` / `checkbox_detector`: 検出0件は例外ではなく空リスト / No detection = empty list, not exception
- `acroform_writer`: 書き込み失敗時は 500 相当の例外 / Write failure = exception mapped to 500
- `api_server`: 例外種別に応じて 422 / 500 を返却 / Returns 422 or 500 depending on exception type

---



## 用語集 / Glossary
Glossary of key terms used in this project. 日本語・英語併記で主要用語を解説します。

| 用語 (JP)         | Term (EN)         | 説明 / Description |
|-------------------|-------------------|--------------------|
| セットアップ       | Setup             | 環境構築手順 / Environment setup steps |
| 疎通確認           | Health check       | サーバーが正常に動作しているかの確認 / Server health verification |
| 依存パッケージ     | Dependencies       | 必要なPythonパッケージ / Required Python packages |
| APIドキュメント     | API docs           | OpenAPI仕様の自動生成ドキュメント / Auto-generated OpenAPI docs |
| 表記ゆれ           | Consistency        | 用語・表現の不統一 / Inconsistent terms or expressions |
| 一意性             | Uniqueness         | 名前や識別子が重複しないこと / No duplicate names or identifiers |
| DPI               | DPI                | 画像解像度の単位（dots per inch）/ Dots per inch, a unit of image resolution |
| API               | API                | アプリケーション間のインターフェース / Application Programming Interface |
| CLI               | CLI                | コマンドラインインターフェース / Command Line Interface |
| AcroForm          | AcroForm           | PDFのフォームフィールド仕様 / PDF form field specification |
| モジュール         | Module             | システムの機能単位 / Functional unit of the system |
| 責務               | Responsibility     | モジュールが担う役割 / Role of the module |
| 差分レビュー       | Diff review        | ドキュメントやコードの変更点を確認する作業 / Reviewing changes in docs or code |
| テンプレート       | Template           | 定型的な記載例 / Standardized example or format |
| Glossary           | Glossary           | 用語集 / List of terms |