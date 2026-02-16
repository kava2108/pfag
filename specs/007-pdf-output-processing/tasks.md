
# Tasks: PDF出力処理（生成フィールドのPDF書き込み・一時ファイル削除・バイナリ返却）

---
## Test-First原則について
このタスクリストはPFAG憲章のTest-First（TDD）原則に従い、
「テストを書く→failを確認→実装→テストpassを確認」の順序で進めることを必須とします。
各User Storyのテストタスクは必ず実装タスクより前に着手し、fail状態を確認してから実装に進んでください。
---

**Input**: specs/007-pdf-output-processing/
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

---

## Phase 1: Setup (Shared Infrastructure)

- [x] T001 [P] プロジェクト構成をplan.md通りに作成・確認
- [x] T002 [P] 必要Pythonパッケージ（FastAPI, PyPDF2, pytest等）をrequirements.txtに追加
- [x] T003 [P] Lint/formatツール（black, isort等）をセットアップ

---

## Phase 2: Foundational (Blocking Prerequisites)

- [x] T004 [P] src/pfag/core/pdf_service.pyに一時ファイル管理・PDF生成基盤を実装
- [x] T005 [P] src/pfag/api/pdf.pyにAPIルーティング・エラーハンドリング基盤を実装
- [x] T006 [P] テスト用サンプルPDF・フィールドJSONをtests/sample/に配置
- [x] T007 [P] pytestのテスト実行環境をtests/unit/conftest.pyで整備

---

## Phase 3: User Story 1 - PDFフィールド書き込み (Priority: P1) 🎯 MVP

**Goal**: 生成済みAcroFormフィールド情報（JSON）を既存PDFに埋め込んだPDFを返却
**Independent Test**: サンプルPDF+フィールドJSONで出力PDFに正しくフォームが埋め込まれること


### Tests（必ず実装前にfailで書くこと）
- [x] T013 [P] [US1] Contractテスト（OpenAPI準拠）をtests/contract/test_pdf_field_writer.pyに実装（failを確認→実装後pass）
- [x] T014 [P] [US1] Integrationテスト（PDF+JSON→PDF）をtests/integration/test_pdf_field_writer.pyに実装（failを確認→実装後pass）
- [x] T015 [P] [US1] 単体テスト（フィールド埋め込み関数）をtests/unit/test_acroform_field_writer.pyに実装（failを確認→実装後pass）

### Implementation（テストfail確認後に着手）
- [x] T008 [P] [US1] src/pfag/core/acroform_field_writer.pyを新規作成（フィールド埋め込みロジック）
- [x] T009 [US1] src/pfag/core/pdf_service.pyからacroform_field_writerを呼び出す処理を追加
- [x] T010 [US1] src/pfag/api/pdf.pyにPOST /pdf/write-fieldsエンドポイントを実装
- [x] T011 [US1] 入力バリデーション・エラー応答をAPIに実装
- [x] T012 [US1] ログ・例外処理を追加

---

## Phase 4: User Story 2 - 一時ファイル削除 (Priority: P2)

**Goal**: 一定期間経過した一時PDF/履歴ファイルを自動削除
**Independent Test**: テスト用一時ファイル作成→削除関数実行で消えること


### Tests（必ず実装前にfailで書くこと）
- [x] T018 [P] [US2] 削除ロジックの単体テストをtests/unit/test_pdf_service.pyに実装（failを確認→実装後pass）
- [x] T019 [P] [US2] 削除API/自動削除の統合テストをtests/integration/test_pdf_service.pyに実装（failを確認→実装後pass）

### Implementation（テストfail確認後に着手）
- [x] T016 [P] [US2] 一時ファイル削除ロジックをsrc/pfag/core/pdf_service.pyに実装
- [x] T017 [US2] 削除APIまたは自動実行タイミングをsrc/pfag/api/pdf.pyに追加

---

## Phase 5: User Story 3 - バイナリ返却 (Priority: P3)

**Goal**: API経由でPDFをバイナリデータとして返却
**Independent Test**: APIでPDF取得し、バイナリ整合性・ダウンロード可能性を確認


### Tests（必ず実装前にfailで書くこと）
- [x] T022 [P] [US3] バイナリ返却のcontractテストをtests/contract/test_pdf_binary.pyに実装（failを確認→実装後pass）
- [x] T023 [P] [US3] バイナリ返却の統合テストをtests/integration/test_pdf_binary.pyに実装（failを確認→実装後pass）

### Implementation（テストfail確認後に着手）
- [x] T020 [P] [US3] バイナリ返却処理をsrc/pfag/api/pdf.pyに実装
- [x] T021 [US3] バイナリ返却時のContent-Type, エラー応答を厳密化

---

## Phase 6: Polish & Cross-Cutting Concerns

- [x] T024 [P] ドキュメント（docs/、quickstart.md等）を最新化
- [x] T025 コードリファクタ・型アノテーション追加
- [x] T026 パフォーマンス最適化・大容量PDF対応
- [x] T027 [P] 追加ユニットテスト（新規バリデーション・エラー分岐・大容量PDF対応等）をtests/unit/に実装し、全分岐網羅を確認
- [x] T028 セキュリティ強化：
	- 入力JSONのスキーマバリデーション（必須項目・型・範囲チェック）
	- 一時ファイルのパーミッション・削除漏れ検証
	- API経由の不正リクエスト・大容量ファイル・DoS耐性テスト
	- テストケースをtests/unit/test_security.pyに実装し、fail→passを確認
- [x] T029 quickstart.md手順で全体動作検証

---

## Dependencies & Execution Order

- Phase 1→2→3以降の順。各User StoryはFoundational完了後に独立・並列実装可
- テスト（[P]）は実装前に作成・fail確認
- 各User Storyは単独でMVP検証可能

## Parallel Execution Examples
- T008, T013, T014, T015は並列可（US1）
- T016, T018, T019は並列可（US2）
- T020, T022, T023は並列可（US3）

## Implementation Strategy
- MVPはUser Story 1（T008〜T015）
- 各ストーリーは独立デプロイ・テスト可能
- 追加ストーリーは順次インクリメンタルに実装
