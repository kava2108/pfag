# Tasks: Agent Skills連携機能

**Input**: Design documents from `/specs/009-agent-skills-integration/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

---

## Phase 1: Setup (Shared Infrastructure)

- [x] T001 Create src/pfag/skills/ ディレクトリと __init__.py
- [x] T002 Initialize Python dependencies (FastAPI, pydantic, pytest) in requirements.txt
- [x] T003 [P] Configure linting/formatting (ruff, black) in pyproject.toml

---

## Phase 2: Foundational (Blocking Prerequisites)

- [x] T004 [P] Create SkillSchemaモデル（Pydantic） in src/pfag/skills/schema.py
- [x] T005 [P] Create SensitivityParamモデル（Pydantic） in src/pfag/skills/sensitivity.py
- [x] T006 [P] Create WarningMessageモデル（Pydantic） in src/pfag/skills/warning.py
- [x] T007 [P] Create SkillWrapperクラス in src/pfag/skills/wrapper.py
- [x] T008 Setup API/CLIルーティング構造 in src/pfag/api/skills.py, src/pfag/cli/skills.py
- [x] T009 Configure error handling/logging in src/pfag/skills/utils.py

---

## Phase 3: User Story 1 - Skillスキーマ定義 (Priority: P1) 🎯 MVP

**Goal**: スキルの入力・出力スキーマを定義・保存できる
**Independent Test**: スキーマ定義機能のみで仕様が記述・保存できること

- [x] T010 [P] [US1] Contract test for /skills POST in tests/contract/test_skills.py
- [x] T011 [P] [US1] Integration test forスキーマ定義 in tests/integration/test_skills.py
- [x] T012 [P] [US1] 実装: SkillSchema保存API in src/pfag/api/skills.py
- [x] T013 [US1] 実装: SkillSchema保存CLI in src/pfag/cli/skills.py
- [x] T014 [US1] SkillSchema保存ロジック in src/pfag/skills/schema.py
- [x] T015 [US1] SkillSchemaバリデーション/エラー説明 in src/pfag/skills/schema.py

---

## Phase 4: User Story 2 - APIラッパ利用 (Priority: P2)

**Goal**: スキーマに基づきAPIラッパで外部API呼び出し
**Independent Test**: ラッパ関数のみでスキーマ通りAPI呼び出しできる

- [x] T016 [P] [US2] Contract test for /skills/{skill_name}/call POST in tests/contract/test_skills_call.py
- [x] T017 [P] [US2] Integration test for APIラッパ in tests/integration/test_skills_call.py
- [x] T018 [P] [US2] SkillWrapper.call実装 in src/pfag/skills/wrapper.py
- [x] T019 [US2] SkillWrapperバリデーション/例外処理 in src/pfag/skills/wrapper.py
- [x] T020 [US2] APIラッパエンドポイント実装 in src/pfag/api/skills.py
- [x] T021 [US2] CLIラッパ実装 in src/pfag/cli/skills.py

---

## Phase 5: User Story 3 - 感度調整・警告説明 (Priority: P3)

**Goal**: 感度調整・警告説明機能の提供
**Independent Test**: 感度調整・警告説明のみでユーザーが挙動を理解・調整できる

- [x] T022 [P] [US3] Contract test for /warnings GET in tests/contract/test_warnings.py
- [x] T023 [P] [US3] Integration test for感度調整・警告説明 in tests/integration/test_warnings.py
- [x] T024 [P] [US3] SensitivityParamロジック実装 in src/pfag/skills/sensitivity.py
- [x] T025 [US3] 警告説明API実装 in src/pfag/api/skills.py
- [x] T026 [US3] 警告説明CLI実装 in src/pfag/cli/skills.py
- [x] T027 [US3] 警告説明ロジック in src/pfag/skills/warning.py

---

## Phase 6: Polish & Cross-Cutting Concerns

- [x] T028 [P] ドキュメント更新 in docs/module-design.md, docs/pdf_rendering.md
- [x] T029 コードリファクタ・型アノテーション強化 in src/pfag/skills/
- [x] T030 [P] 追加ユニットテスト in tests/unit/
- [x] T031 パフォーマンス・セキュリティ最適化
- [x] T032 quickstart.md検証

---

## Dependencies & Execution Order

- Phase 1→2→3/4/5（Foundational完了後は各US並列可）
- 各User Storyは独立テスト可能
- [P]タスクは異ファイル・依存なしで並列実行可

## Parallel Execution Examples

- T004〜T007は同時着手可
- 各User Storyのテスト・モデル・サービスは並列化可
- T010/T011, T016/T017, T022/T023は同時実行可

## Implementation Strategy

- MVPはUser Story 1（スキーマ定義）
- 以降、US2, US3を独立追加・検証
- 各Phaseごとに独立デモ・検証可能
