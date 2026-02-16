## Edge Cases / Error Handling

- 無効な座標・サイズ指定時はAPIレスポンスで明確なエラーメッセージとHTTP 400エラーコードを返す
- 既存フィールド名と重複する場合はHTTP 409エラーコードとエラーメッセージを返す

## Clarifications
### Session 2026-02-16
- Q: フィールド追加時の位置・サイズ指定方法は？ → A: APIパラメータで座標・寸法を明示的に指定（x, y, width, height）
- Q: エラー時の挙動（無効な座標や重複名など）は？ → A: APIレスポンスで明確なエラーメッセージ＋HTTPエラーコード（400/409等）を返す
# Feature Specification: AcroFormフィールド生成

**Feature Branch**: `006-acroform-field-generation`
**Created**: 2026-02-16
**Status**: Draft
**Input**: User description: "AcroFormフィールド生成機能の実装。/Tx（テキストフィールド）と/Btn（チェックボックス）の生成、appendモード、命名規則field_p{page}_{type}{index}、Acrobatで正常入力可能なPDF生成を含む。"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - テキストフィールド生成 (Priority: P1)

ユーザーはPDFに新しいテキストフィールド（/Tx）を追加できる。

**Why this priority**: テキスト入力欄はAcroFormの基本機能であり、最も利用頻度が高い。

**Independent Test**: テキストフィールドを追加したPDFをAcrobatで開き、入力・保存ができることを確認する。

**Acceptance Scenarios**:

1. **Given** 空のPDF、**When** テキストフィールドを追加、**Then** Acrobatで編集可能なテキスト欄が表示される
2. **Given** 既存AcroForm付きPDF、**When** appendモードでテキストフィールドを追加、**Then** 既存フィールドを壊さず新フィールドが追加される

---

### User Story 2 - チェックボックス生成 (Priority: P2)

ユーザーはPDFに新しいチェックボックス（/Btn）を追加できる。

**Why this priority**: チェックボックスもフォームでよく使われる要素であり、実用性が高い。

**Independent Test**: チェックボックスを追加したPDFをAcrobatで開き、チェック・保存ができることを確認する。

**Acceptance Scenarios**:

1. **Given** 空のPDF、**When** チェックボックスを追加、**Then** Acrobatで操作可能なチェックボックスが表示される
2. **Given** 既存AcroForm付きPDF、**When** appendモードでチェックボックスを追加、**Then** 既存フィールドを壊さず新フィールドが追加される

---

### User Story 3 - 命名規則の適用 (Priority: P3)

フィールド名が `field_p{page}_{type}{index}` 形式で自動命名される。

**Why this priority**: 命名規則の統一により、後続処理や識別が容易になるため。

**Independent Test**: 追加されたフィールドの名前が命名規則に従っていることを確認する。

**Acceptance Scenarios**:

1. **Given** 複数フィールド追加時、**When** それぞれ追加、**Then** 命名規則通りの名前が付与される

---

## Functional Requirements

1. PDFに/Tx（テキストフィールド）を追加できること
2. PDFに/Btn（チェックボックス）を追加できること
3. 既存AcroFormがある場合、既存フィールドを壊さずappendできること
4. フィールド名は `field_p{page}_{type}{index}` 形式で自動付与されること
5. 生成されたPDFがAcrobatで正常に入力・保存可能であること

## Success Criteria

- テキストフィールド・チェックボックスを追加したPDFがAcrobat Pro/Reader最新版、Chrome最新版、Edge最新版で編集・保存可能である
- 既存AcroForm付きPDFに対してもフィールド追加が壊れず行える
- 追加フィールドの命名がすべて命名規則に従っている
- 上記3種の主要PDFビューアでフォーム入力・保存ができる

## Key Entities

- PDFファイル
- AcroFormフィールド（/Tx, /Btn）
- フィールド名（field_p{page}_{type}{index}）


## Assumptions

- PDFはAcrobat互換の仕様に準拠している
- appendモード時、既存フィールド情報は保持される
- フィールド追加時の位置・サイズ指定は「APIパラメータで座標・寸法（x, y, width, height）を明示的に指定」する
- 1PDFあたり最大100フィールド、ファイルサイズ10MBまでを上限とする
- API認証必須（JWT/Bearer等）、PDFは一時保存のみ、外部公開なし

## Edge Cases / Error Handling

- 無効な座標・サイズ指定時はAPIレスポンスで明確なエラーメッセージとHTTP 400エラーコードを返す
- 既存フィールド名と重複する場合はHTTP 409エラーコードとエラーメッセージを返す
- 1PDFあたり100フィールド超過、または10MB超過時はHTTP 413エラーコード（Payload Too Large）を返す

## Clarifications
### Session 2026-02-16
- Q: フィールド追加時の位置・サイズ指定方法は？ → A: APIパラメータで座標・寸法を明示的に指定（x, y, width, height）
- Q: スケール上限（フィールド数・PDFサイズ）は？ → A: 1PDFあたり最大100フィールド、ファイルサイズ10MBまで
- Q: セキュリティ要件（認証・保存・公開範囲）は？ → A: API認証必須（JWT/Bearer等）、PDFは一時保存のみ、外部公開なし
- Q: 動作確認対象ビューアは？ → A: Acrobat Pro/Reader最新版、Chrome最新版、Edge最新版で動作確認
