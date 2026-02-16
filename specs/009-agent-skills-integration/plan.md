
# Implementation Plan: Agent Skills連携機能

**Branch**: `009-agent-skills-integration` | **Date**: 2026-02-16 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/009-agent-skills-integration/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.


## Summary

本機能は「エージェントスキル」の入力・出力スキーマ定義、スキーマに基づくAPIラッパ、感度調整・警告説明機能を提供する。スキーマはJSON形式、APIラッパはREST APIを主対象とし、感度調整は数値パラメータで制御、警告説明は日本語で返す。技術的にはPython 3.12、FastAPI、pytest、標準JSONバリデーションを想定。


## Technical Context

**Language/Version**: Python 3.12  
**Primary Dependencies**: FastAPI, pytest, 標準json, typing, pydantic（バリデーション用途）  
**Storage**: N/A（ファイルまたはメモリ内、DBは現状不要）  
**Testing**: pytest  
**Target Platform**: Linux server  
**Project Type**: single（src/pfag/配下に実装）  
**Performance Goals**: スキーマ定義・API呼び出しが1秒以内、エラー説明は即時返却  
**Constraints**: constitution準拠（TDD必須、CLI/API両対応、構造化ログ、型アノテーション、外部入力バリデーション）  
**Scale/Scope**: 1サービス・1ライブラリ単位、ユーザー数・スキル数は数十〜数百を想定


## Constitution Check

**GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.**

- [x] Library-First: すべて独立ライブラリ設計・自己完結・テスト・ドキュメント必須
- [x] CLI & API Interface: CLI/API両対応、入出力はテキスト/JSON、人間可読形式サポート
- [x] Test-First: TDD・Red-Green-Refactorサイクル厳守
- [x] Integration Testing: スキーマ・APIラッパ・感度調整は統合テスト必須
- [x] Observability & Versioning: 構造化ログ・MAJOR.MINOR.PATCHバージョン
- [x] Python 3.8+、FastAPI、バリデーション必須、セキュリティ考慮
- [x] ドキュメント・API仕様は常に最新
- [x] PR時にconstitution遵守をレビューチェック
- [x] 複雑化は正当な理由がある場合のみ許容

違反事項なし。Phase 0に進行可能。

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

tests/
ios/ or android/

### Source Code (repository root)

```text
src/
├── pfag/
│   ├── skills/         # スキルスキーマ・ラッパ・感度調整ロジック
│   ├── api/            # APIエンドポイント
│   ├── cli/            # CLIインターフェース
│   └── utils/          # 汎用ユーティリティ
tests/
├── contract/
├── integration/
└── unit/
```

**Structure Decision**: src/pfag/skills/配下にスキルスキーマ・ラッパ・感度調整ロジックを実装。API/CLI/ユーティリティは既存構成を踏襲。テストはcontract/integration/unitで分離。

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
