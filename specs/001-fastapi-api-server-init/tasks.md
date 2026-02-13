---

description: "Task list for FastAPI APIサーバー初期化 feature"
---

# Tasks: FastAPI APIサーバー初期化

**Input**: Design documents from `/specs/001-fastapi-api-server-init/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 Create project structure per implementation plan (src/pfag/, api/, core/, utils/)
- [X] T002 Initialize Python project with FastAPI and uvicorn dependencies (pyproject.toml or requirements.txt)
- [X] T003 [P] Configure linting and formatting tools (e.g., black, isort) in pyproject.toml

---

## Phase 2: Foundational (Blocking Prerequisites)

- [X] T004 Setup base FastAPI app in src/pfag/api/main.py
- [X] T005 [P] Setup API routing structure in src/pfag/api/main.py
- [X] T006 [P] Create __init__.py files in src/pfag/, api/, core/, utils/
- [X] T007 Configure error handling for startup failures (src/pfag/api/main.py)
- [X] T008 Setup environment configuration (src/pfag/core/config.py)

---

## Phase 3: User Story 1 - APIサーバーの起動 (Priority: P1) 🎯 MVP

**Goal**: FastAPIサーバーをコマンド一つで起動し、/healthエンドポイントでJSON { "status": "ok" } を返す

**Independent Test**: uvicornで起動後、/healthにアクセスし200+JSON応答を確認

### Implementation for User Story 1

- [X] T009 [P] [US1] Implement /health endpoint in src/pfag/api/main.py
- [X] T010 [US1] Add OpenAPI contract for /health in contracts/openapi.yaml
- [X] T011 [US1] Add contract test for /health in tests/contract/test_health.py
- [X] T012 [US1] Add integration test for server startup and /health in tests/integration/test_server.py
- [X] T013 [US1] Add logging for /health access in src/pfag/api/main.py

---

## Phase 4: User Story 2 - 開発者の初期導入 (Priority: P2)

**Goal**: 新規開発者が最小限の手順でAPIサーバーを起動できる

**Independent Test**: quickstart.md/README通りにセットアップし、サーバー起動・/health応答を確認

### Implementation for User Story 2

- [X] T014 [P] [US2] Document setup steps in quickstart.md and README.md
- [X] T015 [US2] Add dependency installation instructions in quickstart.md
- [X] T016 [US2] Add example uvicorn command in quickstart.md
- [X] T017 [US2] Add troubleshooting section for port conflicts and missing dependencies in quickstart.md

---

## Phase N: Polish & Cross-Cutting Concerns

- [X] T018 [P] Documentation updates in docs/
- [X] T019 Code cleanup and refactoring
- [X] T020 Performance optimization (if needed)
- [X] T021 [P] Additional unit tests in tests/unit/
- [X] T022 Security hardening
- [X] T023 Run quickstart.md validation

---

## Dependencies & Execution Order

- Phase 1 → Phase 2 → Phase 3 (US1) → Phase 4 (US2) → Polish
- US1, US2は独立してテスト可能
- US1がMVP

## Parallel Opportunities

- T003, T005, T006, T009, T014, T018, T021は並列実行可能
- US1, US2はPhase 2完了後並列実装可能

## Implementation Strategy

- MVP: Phase 1→2→3（US1）で/health応答まで
- Incremental: US2以降は独立追加

---

# Format validation

- 全タスクがチェックリスト形式（- [ ] Txxx [P] [USx] 説明 ファイルパス）
- 各タスクはファイルパス明記
- 並列可能タスクは[P]付き
- User Storyごとに独立テスト基準あり
- MVPはUS1
