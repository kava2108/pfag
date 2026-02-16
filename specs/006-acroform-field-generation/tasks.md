---

description: "Task list for AcroFormフィールド生成 (006-acroform-field-generation)"
---

# Tasks: AcroFormフィールド生成

**Input**: Design documents from `/specs/006-acroform-field-generation/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 Create project structure per implementation plan
- [X] T002 Initialize Python project with FastAPI, PyPDF2, WeasyPrint, Pillow, numpy
- [X] T003 [P] Configure linting and formatting tools (black, isort)

---

## Phase 2: Foundational (Blocking Prerequisites)

- [X] T004 [P] Setup API routing and middleware structure in src/pfag/api/main.py
- [X] T005 [P] Implement authentication middleware (JWT/Bearer) in src/pfag/api/main.py
- [X] T006 [P] Create AcroFormField data model in src/pfag/core/pdf_service.py
- [X] T007 Configure error handling and logging in src/pfag/api/main.py
- [X] T008 Setup environment configuration in src/pfag/core/config.py

---

## Phase 3: User Story 1 - テキストフィールド生成 (Priority: P1) 🎯 MVP

**Goal**: PDFに新しいテキストフィールド（/Tx）を追加できる
**Independent Test**: テキストフィールドを追加したPDFをAcrobatで開き、入力・保存ができること

- [X] T009 [P] [US1] Contract test for /v1/acroform/fields in tests/contract/test_pdf.py
- [X] T010 [P] [US1] Integration test for テキストフィールド追加 in tests/integration/test_pdf.py
- [X] T011 [P] [US1] Create PDF entity and page model in src/pfag/core/pdf_service.py
- [X] T012 [P] [US1] Implement /Txフィールド生成ロジック in src/pfag/core/pdf_service.py
- [X] T013 [US1] Implement /v1/acroform/fields endpoint (テキストフィールド) in src/pfag/api/pdf.py
- [X] T014 [US1] Add validation and error handling for /Tx in src/pfag/api/pdf.py
- [X] T015 [US1] Add logging for テキストフィールド生成 in src/pfag/api/pdf.py

---

## Phase 4: User Story 2 - チェックボックス生成 (Priority: P2)

**Goal**: PDFに新しいチェックボックス（/Btn）を追加できる
**Independent Test**: チェックボックスを追加したPDFをAcrobatで開き、チェック・保存ができること

- [X] T016 [P] [US2] Contract test for /v1/acroform/fields (Btn) in tests/contract/test_checkbox_detection.py
- [X] T017 [P] [US2] Integration test for チェックボックス追加 in tests/integration/test_pdf.py
- [X] T018 [P] [US2] Implement /Btnフィールド生成ロジック in src/pfag/core/checkbox_detection.py
- [X] T019 [US2] Implement /v1/acroform/fields endpoint (チェックボックス) in src/pfag/api/checkbox.py
- [X] T020 [US2] Add validation and error handling for /Btn in src/pfag/api/checkbox.py
- [X] T021 [US2] Add logging for チェックボックス生成 in src/pfag/api/checkbox.py

---

## Phase 5: User Story 3 - 命名規則の適用 (Priority: P3)

**Goal**: フィールド名が `field_p{page}_{type}{index}` 形式で自動命名される
**Independent Test**: 追加されたフィールドの名前が命名規則に従っていること

- [X] T022 [P] [US3] Contract test for 命名規則 in tests/contract/test_pdf.py
- [X] T023 [P] [US3] Integration test for 命名規則 in tests/integration/test_pdf.py
- [X] T024 [P] [US3] Implement 命名規則ロジック in src/pfag/core/pdf_service.py
- [X] T025 [US3] Add validation for 命名規則 in src/pfag/api/pdf.py

---

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T026 [P] Documentation updates in docs/pdf_rendering.md
- [X] T027 Code cleanup and refactoring
- [X] T028 Performance optimization across all stories
- [X] T029 [P] Additional unit tests in tests/unit/
- [X] T030 Security hardening
- [X] T031 Run quickstart.md validation

---

## Dependencies & Execution Order

- Phase 1 → Phase 2 → Phase 3/4/5 (USごとに独立並列可) → Phase 6
- US1, US2, US3はFoundational完了後に並列実装可能

## Parallel Execution Examples

- T009, T010, T011, T012は並列実行可（US1）
- T016, T017, T018は並列実行可（US2）
- T022, T023, T024は並列実行可（US3）

## Implementation Strategy

- MVP: Phase 3（US1）までで最小価値を検証
- 以降、US2, US3を独立追加・検証
- 各USは独立テスト・デプロイ可能
