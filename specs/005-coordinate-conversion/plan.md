# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

座標変換（画像座標 → PDF座標）機能の実装。画像サイズ（px）・PDFサイズ（pt）を取得し、X/Y座標変換式で座標を変換。誤差許容範囲は±2pt。アスペクト比差異の検証・単体テストで精度保証。

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.11  
**Primary Dependencies**: Pillow (PIL), PyPDF2, numpy  
**Storage**: N/A（座標変換のみ）  
**Testing**: pytest  
**Target Platform**: Linux server  
**Project Type**: single（core/utils/cli構成）  
**Performance Goals**: 1座標変換あたり1秒以内  
**Constraints**: 誤差±2pt以内、画像・PDFサイズ取得必須  
**Scale/Scope**: 単体テスト・CLI/サービスで利用

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

GATE: Library-First（座標変換ロジックはcore/utilsに独立実装）
GATE: CLI Interface（座標変換はCLI/サービスから呼び出し可能）
GATE: Test-First（pytestによる単体テスト必須）
GATE: Integration Testing（PDF/画像サイズ取得・座標変換の契約テスト）
GATE: Observability（ログ出力・エラー時の明示的通知）

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
# [REMOVE IF UNUSED] Option 1: Single project (DEFAULT)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# [REMOVE IF UNUSED] Option 2: Web application (when "frontend" + "backend" detected)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# [REMOVE IF UNUSED] Option 3: Mobile + API (when "iOS/Android" detected)
api/
└── [same as backend above]

ios/ or android/
└── [platform-specific structure: feature modules, UI flows, platform tests]
```

**Structure Decision**: [Document the selected structure and reference the real
directories captured above]

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
