# Data Model: AcroFormフィールド生成

## Entity: PDF
- id: string (ファイル名またはUUID)
- pages: List[PDFPage]

## Entity: PDFPage
- number: int
- fields: List[AcroFormField]

## Entity: AcroFormField
- name: string (例: field_p1_Tx1)
- type: string (Tx or Btn)
- page: int
- rect: [float, float, float, float]  # x, y, width, height
- value: string | bool | None
- required: bool (default: False)
- options: dict (拡張用)

## Validation Rules
- nameはfield_p{page}_{type}{index}形式で一意
- rectはページ内で重複・はみ出し不可
- typeはTx（テキスト）またはBtn（チェックボックス）のみ
- 1PDFあたり100フィールド/10MB上限

## State Transitions
- 新規PDF: fields=[]
- append時: 既存fields + 新規fields
- エラー時: バリデーション失敗でAPIエラー返却
