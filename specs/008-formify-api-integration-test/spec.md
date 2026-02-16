# Feature Specification: formify API integration test

**Feature Branch**: `008-formify-api-integration-test`  
**Created**: 2026-02-16  
**Status**: Draft  
**Input**: User description: "formify APIの統合テストを作成し、API仕様に沿った動作を検証する"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - 正常系PDFフォーム化 (Priority: P1)

ユーザーがPDFファイルとオプションJSONをmultipart/form-dataでアップロードし、正常にPDFフォーム化レスポンスを受け取る。

**Why this priority**: APIの基本機能であり、最も重要なユースケース。

**Independent Test**: テスト用PDFとオプションを送信し、200レスポンス・PDFバイナリが返ることを確認。

**Acceptance Scenarios**:
1. **Given** 有効なPDFと正しいoptions、**When** /v1/formifyにPOST、**Then** 200・PDFバイナリ返却
2. **Given** 有効なPDFのみ、**When** /v1/formifyにPOST、**Then** 200・PDFバイナリ返却

---

### User Story 2 - ファイル未指定・不正 (Priority: P2)

ファイルが未指定または空の場合、422エラーが返る。

**Why this priority**: 入力バリデーションの基本。

**Independent Test**: ファイル無しでPOSTし、422エラーを確認。

**Acceptance Scenarios**:
1. **Given** ファイル無し、**When** /v1/formifyにPOST、**Then** 422エラー
2. **Given** 空ファイル、**When** /v1/formifyにPOST、**Then** 422エラー

---

### User Story 3 - options JSON不正 (Priority: P3)

optionsが不正JSONの場合、422エラーが返る。

**Why this priority**: オプション解析の堅牢性担保。

**Independent Test**: 不正なoptionsでPOSTし、422エラーを確認。

**Acceptance Scenarios**:
1. **Given** 不正JSONのoptions、**When** /v1/formifyにPOST、**Then** 422エラー

---

### User Story 4 - 検出0件時の警告 (Priority: P4)

検出0件時、X-PFAG-Warningヘッダが付与される。

**Why this priority**: ユーザーへのフィードバック向上。

**Independent Test**: 検出0件となる入力でPOSTし、ヘッダを確認。

**Acceptance Scenarios**:
1. **Given** 検出0件となるPDF、**When** /v1/formifyにPOST、**Then** 200・X-PFAG-Warningヘッダ

---

## Functional Requirements

1. multipart/form-dataでPDFファイルとoptions(JSON)を受信できること
2. optionsのdetection_mode, sensitivity, output_prefixを正しく解釈できること
3. ファイル未指定・空・不正時は422エラーを返すこと
4. optionsが不正JSONの場合は422エラーを返すこと
5. 検出0件時はX-PFAG-Warningヘッダを返すこと
6. 正常時は200・PDFバイナリを返すこと
7. サーバ内部エラー時は500エラーを返すこと

## Success Criteria

- すべてのユーザーストーリーが独立してテスト可能である
- 主要な異常系（422, 500）が網羅されている
- X-PFAG-Warningヘッダの有無が正しく判定できる
- 仕様通りのレスポンス（バイナリ/エラー/ヘッダ）が返る
- テストは自動化され、CIで再現可能

## Key Entities

- PDFファイル
- options(JSON: detection_mode, sensitivity, output_prefix)
- レスポンス（PDFバイナリ, エラーメッセージ, ヘッダ）


## Assumptions

- 検出処理はダミー実装（常に0件）
- PDFバイナリはダミーで十分
- CI環境でpytestが利用可能

## Clarifications

### Session 2026-02-16
- Q: このAPI統合テストはCI/CDパイプラインでの自動実行のみを想定し、パフォーマンス・スケーラビリティ・セキュリティ等の非機能要件は本仕様のスコープ外とするか？ → A: 非機能要件（パフォーマンス・スケーラビリティ等）は本仕様のスコープ外とする

### Out of Scope
- 本仕様ではパフォーマンス、スケーラビリティ、セキュリティ、可用性、監視、法令遵守等の非機能要件は明示的に対象外とする。必要に応じて別途仕様化する。
