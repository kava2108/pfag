---
description: "Task list for coordinate conversion feature implementation"
---

# Tasks: 座標変換（画像座標 → PDF座標）

**Input**: Design documents from `/specs/005-coordinate-conversion/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 Create project structure for coordinate conversion in src/pfag/core/
- [X] T002 Initialize Python project dependencies (Pillow, PyPDF2, numpy) in requirements.txt
- [X] T003 [P] Configure pytest for unit testing in tests/unit/

---

## Phase 2: Foundational (Blocking Prerequisites)

- [X] T004 Create coordinate conversion entity definitions in src/pfag/core/coordinate_conversion.py
- [X] T005 [P] Implement input validation logic in src/pfag/core/coordinate_conversion.py
- [X] T006 [P] Setup CLI entrypoint for coordinate conversion in src/pfag/cli/coordinate_convert.py
- [X] T007 Setup logging and error handling in src/pfag/core/coordinate_conversion.py

---

## Phase 3: User Story 1 - 座標変換結果の取得 (Priority: P1) 🎯 MVP

**Goal**: 画像座標をPDF座標に正確に変換する
**Independent Test**: サンプル画像・PDFで座標変換結果が期待値と一致する

### Tests for User Story 1
- [X] T008 [P] [US1] Contract test for POST /coordinate-convert in tests/contract/test_coordinate_conversion.py
- [X] T009 [P] [US1] Unit test for coordinate conversion logic in tests/unit/test_coordinate_conversion.py

### Implementation for User Story 1
- [X] T010 [P] [US1] Implement coordinate conversion function in src/pfag/core/coordinate_conversion.py
- [X] T011 [US1] Integrate coordinate conversion with CLI in src/pfag/cli/coordinate_convert.py
- [X] T012 [US1] Implement API endpoint in src/pfag/api/coordinate.py
- [X] T013 [US1] Add error handling and logging for conversion

---

## Phase 4: User Story 2 - アスペクト比差異の検証 (Priority: P2)

**Goal**: アスペクト比差異による変換誤差を検証
**Independent Test**: アスペクト比が異なる画像・PDFで誤差が許容範囲内か確認

### Tests for User Story 2
- [X] T014 [P] [US2] Unit test for aspect ratio difference in tests/unit/test_coordinate_conversion.py

### Implementation for User Story 2
- [X] T015 [P] [US2] Implement aspect ratio check logic in src/pfag/core/coordinate_conversion.py
- [X] T016 [US2] Integrate aspect ratio warning in CLI/API in src/pfag/cli/coordinate_convert.py, src/pfag/api/coordinate.py

---

## Phase 5: User Story 3 - 単体テストによる検証 (Priority: P3)

**Goal**: 座標変換ロジックの単体テストで誤差が許容範囲内であることを確認
**Independent Test**: テストケースで座標変換結果の誤差を計測し、許容範囲内か確認

### Tests for User Story 3
- [X] T017 [P] [US3] Unit test for conversion error margin in tests/unit/test_coordinate_conversion.py

### Implementation for User Story 3
- [X] T018 [P] [US3] Implement error margin calculation in src/pfag/core/coordinate_conversion.py
- [X] T019 [US3] Integrate error margin validation in CLI/API in src/pfag/cli/coordinate_convert.py, src/pfag/api/coordinate.py

---

## Final Phase: Polish & Cross-Cutting Concerns

- [X] T020 [P] Documentation updates in docs/pdf_rendering.md
- [X] T021 Code cleanup and refactoring in src/pfag/core/coordinate_conversion.py
- [X] T022 Performance optimization for coordinate conversion
- [X] T023 [P] Additional unit tests in tests/unit/test_coordinate_conversion.py
- [X] T024 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies
- Setup (Phase 1): No dependencies
- Foundational (Phase 2): Depends on Setup completion
- User Stories (Phase 3+): Depend on Foundational phase completion
- Polish (Final Phase): Depends on all user stories being complete

### User Story Dependencies
- User Story 1 (P1): Can start after Foundational
- User Story 2 (P2): Can start after Foundational
- User Story 3 (P3): Can start after Foundational

### Parallel Opportunities
- [P] tasks: T003, T005, T006, T008, T009, T010, T014, T015, T017, T018, T020, T023
- User stories can be implemented independently after Foundational

---

## Implementation Strategy

- MVP first: Phase 1 → Phase 2 → Phase 3 (US1)
- Incremental delivery: Phase 4 (US2), Phase 5 (US3)
- Parallel: [P] tasks and user stories

