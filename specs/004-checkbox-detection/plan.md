
# Implementation Plan: チェックボックス検出（矩形検出）

**Branch**: `004-checkbox-detection` | **Date**: 2026-02-14 | **Spec**: [specs/004-checkbox-detection/spec.md](specs/004-checkbox-detection/spec.md)
**Input**: Feature specification from `/specs/004-checkbox-detection/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

画像またはPDFから手書き・印刷のチェックボックス（四角形）を検出し、各ボックスの座標・サイズ・塗りつぶし状態（ON/OFF）を返す。帳票やアンケートの自動読取用途。水平・垂直に近い矩形のみ対象、ノイズや非矩形は除外。API・CLI・テスト・サンプル画像も含む。

## Technical Context

**Language/Version**: Python 3.11  
**Primary Dependencies**: OpenCV, NumPy, PyMuPDF, Pillow, FastAPI  
**Storage**: N/A（ファイル入出力のみ）  
**Testing**: pytest, FastAPI TestClient  
**Target Platform**: Linux server, cross-platform  
**Project Type**: single (src/pfag/...)  
**Performance Goals**: 画像1枚あたり3秒以内で検出  
**Constraints**: 入力画像サイズ上限あり（1200x1200px程度）、矩形サイズ・比率閾値あり  
**Scale/Scope**: 帳票1枚〜数百枚/バッチ、同時APIリクエスト数は少数想定

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ライブラリ本体・CLI・API・テスト・サンプル画像を分離実装（Library-First, CLI Interface, Test-First）
- TDD必須（テスト→実装→リファクタ）
- CLI/JSON I/O・構造化ログ必須
- コントラクトテスト・サンプルデータ必須
- 複雑化・多層化は最小限、単一src配下で管理

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

tests/
ios/ or android/

```text
src/pfag/core/checkbox_detection.py      # サービス本体
src/pfag/cli/checkbox_detect.py          # CLI
src/pfag/api/checkbox.py                 # FastAPIエンドポイント
tests/unit/test_checkbox_detection.py     # 単体テスト
tests/contract/test_checkbox_detection.py # コントラクトテスト
tests/sample/generate_checkbox_images.py  # サンプル画像生成
specs/004-checkbox-detection/             # ドキュメント・設計
```

**Structure Decision**: src/pfag/配下にcore・cli・apiを分離、tests/配下にunit・contract・sampleを分離。specs/配下に設計・契約・タスク管理を集約。


## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|

