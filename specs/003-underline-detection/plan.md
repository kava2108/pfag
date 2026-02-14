# Implementation Plan: 下線検出（テキストフィールド）

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

[Extract from feature spec: primary requirement + technical approach from research]

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.11  
**Primary Dependencies**: OpenCV, NumPy, PyMuPDF, Pillow  
**Storage**: N/A（ファイル/メモリのみ）  
**Testing**: pytest  
**Target Platform**: Linux server
**Project Type**: single  
**Performance Goals**: 1画像あたり1秒以内（1000x1000px）  
**Constraints**: メモリ消費<200MB、外部入力バリデーション必須  
**Scale/Scope**: 1画像単位、1000x1000pxまで

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- TDD必須（テスト→実装→リファクタ）
- CLI/ライブラリ分離（CLI必須なら明記）
- すべての機能は独立テスト可能
- ログ出力・バリデーション必須

## Project Structure

### Documentation (this feature)


```text
specs/003-underline-detection/
├── plan.md              # このファイル
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
src/pfag/core/underline_detection.py（サービス本体）
src/pfag/cli/underline_detect.py（CLI/バッチ用）
tests/unit/test_underline_detection.py
tests/contract/test_underline_detection.py
specs/003-underline-detection/（plan, research, data-model, quickstart, contracts, tasks）
```

**Structure Decision**: src/pfag/core/underline_detection.pyを中心としたシングルプロジェクト構成。CLI・テスト・ドキュメントも分離配置。

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
