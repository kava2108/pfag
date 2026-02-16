# Implementation Plan: PDF出力処理（生成フィールドのPDF書き込み・一時ファイル削除・バイナリ返却）

**Branch**: `007-pdf-output-processing` | **Date**: 2026-02-16 | **Spec**: [specs/007-pdf-output-processing/spec.md](specs/007-pdf-output-processing/spec.md)
**Input**: Feature specification from `/specs/007-pdf-output-processing/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

本機能は、生成済みAcroFormフィールド情報（JSON形式）を既存PDFに埋め込み、バイナリとして返却するAPIを提供する。加えて、一時ファイルの自動削除機能も実装する。技術的にはPyPDF2/pdfrw等でAcroForm編集、FastAPIでAPI化、TemporaryDirectory管理でセキュリティ担保を行う。


## Technical Context

**Language/Version**: Python 3.8+  
**Primary Dependencies**: FastAPI, PyPDF2 or pdfrw, TemporaryDirectory, JSON  
**Storage**: 一時ファイル（OS temp dir）、永続ストレージ不要  
**Testing**: pytest（unit, contract, integration）  
**Target Platform**: Linux server  
**Project Type**: single (backend API)  
**Performance Goals**: 1リクエストあたり2秒以内、100MB未満/ファイル  
**Constraints**: 一時ファイルは即時削除、外部入力はバリデーション必須  
**Scale/Scope**: 1リクエスト=1PDF、同時10リクエスト程度を想定


## Constitution Check

**Library-First**: PDFフィールド埋め込み・一時ファイル管理は独立モジュール化し、テスト・CLI化も考慮する。
**CLI/API Interface**: API（FastAPI）とCLI両対応を目指す。入出力はJSON/バイナリ。
**Test-First**: 仕様に基づきテストケースを先行作成。
**Integration Testing**: API/CLI/内部関数の統合テストを必須とする。
**Observability/Versioning**: ログ・エラー出力・バージョン付与を徹底。

**GATE**: 憲章違反なし。全要件は実装計画・設計段階で再チェック。

## Project Structure


### Documentation (this feature)

```text
specs/007-pdf-output-processing/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
└── tasks.md
```


### Source Code (repository root)

```text
src/pfag/
├── api/
│   └── pdf.py（APIエンドポイント）
├── core/
│   ├── pdf_service.py（一時ファイル管理・PDF生成）
│   └── acroform_field_writer.py（新規: フィールド埋め込み）
└── utils/

tests/
├── contract/
├── integration/
└── unit/
```

**Structure Decision**: シングルプロジェクト構成。src/pfag/core/に機能別モジュールを配置し、API層・テスト層と分離。
