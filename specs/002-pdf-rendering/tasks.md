---
description: "Tasks for PDFレンダリング (002-pdf-rendering)"
---

# Tasks: PDFレンダリング

**Input**: Design documents from `/specs/002-pdf-rendering/`
**Prerequisites**: plan.md, spec.md, contracts/openapi.yaml

## Phase 1: Setup (Shared Infrastructure)

- [ ] T001 Create src/pfag/api/pdf.py and src/pfag/core/pdf_service.py per plan.md
- [ ] T002 Initialize PDF生成用ライブラリ (WeasyPrint, PyPDF2) in requirements.txt/pyproject.toml
- [ ] T003 [P] Setup tests/contract, tests/integration, tests/unit structure

---

## Phase 2: Foundational (Blocking Prerequisites)

- [ ] T004 Setup FastAPIルーティング基盤 in src/pfag/api/pdf.py
- [ ] T005 [P] 共通エラーハンドリング/レスポンス設計 in src/pfag/api/pdf.py
- [ ] T006 [P] PDF一時保存ディレクトリ管理 in src/pfag/core/pdf_service.py

---

## Phase 3: User Story 1 - HTML→PDF変換API (Priority: P1) 🎯 MVP

**Goal**: HTMLデータをPOSTし、PDFファイルをダウンロードできるAPIを提供
**Independent Test**: サンプルHTMLをPOSTし、PDFがダウンロードできること

### Tests for User Story 1
- [ ] T007 [P] [US1] Contract test for /pdf in tests/contract/test_pdf.py
- [ ] T008 [P] [US1] Integration test for HTML→PDF変換 in tests/integration/test_pdf.py

### Implementation for User Story 1
- [ ] T009 [P] [US1] PDF生成サービスクラス実装 in src/pfag/core/pdf_service.py
- [ ] T010 [US1] /pdfエンドポイント実装 in src/pfag/api/pdf.py
- [ ] T011 [US1] バリデーション・エラーハンドリング in src/pfag/api/pdf.py
- [ ] T012 [US1] PDF生成ファイルの一時保存 in src/pfag/core/pdf_service.py

---

## Phase 4: User Story 2 - PDFプレビュー (Priority: P2)

**Goal**: 生成済みPDFをWeb上で直接プレビュー表示できるAPIを提供
**Independent Test**: /pdf/previewでPDFが直接表示されること

### Tests for User Story 2
- [ ] T013 [P] [US2] Contract test for /pdf/preview in tests/contract/test_pdf_preview.py
- [ ] T014 [P] [US2] Integration test for PDFプレビュー in tests/integration/test_pdf_preview.py

### Implementation for User Story 2
- [ ] T015 [US2] PDFプレビュー用サービス実装 in src/pfag/core/pdf_service.py
- [ ] T016 [US2] /pdf/previewエンドポイント実装 in src/pfag/api/pdf.py
- [ ] T017 [US2] プレビュー用PDF取得・エラー処理 in src/pfag/core/pdf_service.py

---

## Phase 5: User Story 3 - PDF生成履歴取得 (Priority: P3)

**Goal**: 生成済みPDFの履歴一覧を取得できるAPIを提供
**Independent Test**: /pdf/historyで履歴がJSONで取得できること

### Tests for User Story 3
- [ ] T018 [P] [US3] Contract test for /pdf/history in tests/contract/test_pdf_history.py
- [ ] T019 [P] [US3] Integration test for PDF履歴取得 in tests/integration/test_pdf_history.py

### Implementation for User Story 3
- [ ] T020 [US3] 履歴管理サービス実装 in src/pfag/core/pdf_service.py
- [ ] T021 [US3] /pdf/historyエンドポイント実装 in src/pfag/api/pdf.py
- [ ] T022 [US3] 履歴データの保存・取得 in src/pfag/core/pdf_service.py

---

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T023 [P] ドキュメント整備 in docs/
- [ ] T024 コードリファクタ・型アノテーション in src/pfag/
- [ ] T025 パフォーマンス・セキュリティ改善 in src/pfag/core/pdf_service.py
- [ ] T026 [P] 追加ユニットテスト in tests/unit/
- [ ] T027 quickstart.md検証・更新 in specs/002-pdf-rendering/quickstart.md

---

## Dependencies & Execution Order

- Phase 1→2→3→4→5→6 の順で進行
- 各User StoryはFoundational完了後、独立して並行実装可能

## Parallel Execution Examples

- テスト・モデル・サービス実装は[P]で並行可能
- 各User Storyのテスト・実装は独立して進行可

## Implementation Strategy

- MVPはUser Story 1（HTML→PDF変換API）
- 以降、User Story 2, 3を独立追加
- 各Storyごとに独立検証・デプロイ可能
