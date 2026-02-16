---

description: "Task list for formify API integration test"
---

# Tasks: formify API integration test

**Input**: Design documents from `/specs/008-formify-api-integration-test/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

## Phase 1: Setup (Shared Infrastructure)

- [x] T001 Create project structure per plan.md (src/pfag/api/, tests/integration/)
- [x] T002 [P] Install FastAPI, pytest, python-multipart in .venv
- [x] T003 [P] Initialize pytest in tests/integration/

---

## Phase 2: Foundational (Blocking Prerequisites)

- [x] T004 [P] Create FastAPI router in src/pfag/api/formify.py
- [x] T005 [P] Setup /v1/formify POST endpoint in src/pfag/api/formify.py
- [x] T006 [P] Add router to main app in src/pfag/api/main.py
- [x] T007 [P] Create test skeleton in tests/integration/test_formify.py

---

## Phase 3: User Story 1 - 正常系PDFフォーム化 (Priority: P1) 🎯 MVP

**Goal**: ユーザーがPDFファイルとオプションJSONをmultipart/form-dataでアップロードし、正常にPDFフォーム化レスポンスを受け取る
**Independent Test**: テスト用PDFとオプションを送信し、200レスポンス・PDFバイナリが返ることを確認

- [x] T008 [P] [US1] Integration test: 正常系PDFフォーム化 in tests/integration/test_formify.py
- [x] T009 [US1] Implement PDFバリデーション・optionsパース in src/pfag/api/formify.py
- [x] T010 [US1] Implement 200レスポンス（PDFバイナリ返却） in src/pfag/api/formify.py

---

## Phase 4: User Story 2 - ファイル未指定・不正 (Priority: P2)

**Goal**: ファイルが未指定または空の場合、422エラーが返る
**Independent Test**: ファイル無しでPOSTし、422エラーを確認

- [x] T011 [P] [US2] Integration test: ファイル未指定・不正 in tests/integration/test_formify.py
- [x] T012 [US2] Implement 422エラー（ファイル未指定・空） in src/pfag/api/formify.py

---

## Phase 5: User Story 3 - options JSON不正 (Priority: P3)

**Goal**: optionsが不正JSONの場合、422エラーが返る
**Independent Test**: 不正なoptionsでPOSTし、422エラーを確認

- [x] T013 [P] [US3] Integration test: options JSON不正 in tests/integration/test_formify.py
- [x] T014 [US3] Implement 422エラー（options不正JSON） in src/pfag/api/formify.py

---

## Phase 6: User Story 4 - 検出0件時の警告 (Priority: P4)

**Goal**: 検出0件時、X-PFAG-Warningヘッダが付与される
**Independent Test**: 検出0件となる入力でPOSTし、ヘッダを確認

- [x] T015 [P] [US4] Integration test: 検出0件時の警告 in tests/integration/test_formify.py
- [x] T016 [US4] Implement X-PFAG-Warningヘッダ付与 in src/pfag/api/formify.py

---

## Final Phase: Polish & Cross-Cutting Concerns

- [x] T017 [P] Update quickstart.md with test instructions in specs/008-formify-api-integration-test/quickstart.md
- [x] T018 [P] Documentation updates in specs/008-formify-api-integration-test/
- [x] T019 Code cleanup and refactoring in src/pfag/api/formify.py
- [x] T020 Run quickstart.md validation in CI

---

## Dependencies & Execution Order

- Phase 1 → Phase 2 → User Stories (Phase 3-6,独立並列可) → Final Phase
- 各User StoryはFoundational完了後、独立して実装・テスト可能

## Parallel Execution Examples

- T002, T003はT001と並列可
- T004〜T007はFoundational内で並列可
- 各User Storyのテスト・実装は並列可（異なるファイル）

## Implementation Strategy

- MVPはUser Story 1（T008〜T010）
- 各User Storyは独立して追加・検証可能
- テスト→実装→検証の順で進行
