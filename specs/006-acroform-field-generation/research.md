# Research: AcroFormフィールド生成

## 1. PyPDF2によるAcroFormフィールド生成のベストプラクティス
- Decision: PyPDF2を用いて/Tx（テキストフィールド）・/Btn（チェックボックス）を生成する
- Rationale: PyPDF2はAcroFormフィールドの追加・編集に対応し、既存PDFへのappendも可能。公式ドキュメント・StackOverflow等で多数の実装例あり。
- Alternatives considered: pdfrw, pikepdf, ReportLab（AcroForm編集はPyPDF2が最も柔軟）

## 2. 既存AcroFormへのappend処理
- Decision: 既存AcroFormが存在する場合はfields配列に新フィールドを追加し、既存フィールドを壊さないようにmergeする
- Rationale: PyPDF2のAcroForm構造はdict型であり、fields配列のappendで既存情報を保持できる
- Alternatives considered: 新規AcroForm上書き（既存フィールド消失リスクが高いため不採用）

## 3. 命名規則の自動付与
- Decision: field_p{page}_{type}{index}形式をPythonで自動生成。typeはTx/Btn、indexはページ内連番
- Rationale: 一意性・可読性・後続処理の容易さを両立
- Alternatives considered: UUID, ランダム名（可読性・管理性で劣る）

## 4. API設計・エラー処理
- Decision: FastAPIでmultipart/form-data受信、バリデーション失敗時はHTTP 400/409/413で明確なエラー返却
- Rationale: RESTful API設計の標準パターン。OpenAPI記述とも整合
- Alternatives considered: サイレント無視、500系のみ返却（ユーザビリティ・運用性で劣る）

## 5. テスト・検証
- Decision: pytestで単体・統合テスト、Acrobat/Chrome/Edgeで手動検証
- Rationale: 自動テスト＋主要ビューアでの動作確認が品質担保に必須
- Alternatives considered: 手動テストのみ（自動化・再現性で劣る）

## 6. 主要依存ライブラリの選定
- Decision: PyPDF2（AcroForm編集）、FastAPI（API）、WeasyPrint（PDF生成/画像化）、Pillow/numpy（画像処理）
- Rationale: 既存コードベース・要件・実績から最適
- Alternatives considered: pdfrw, pikepdf, Flask等

## 7. セキュリティ・スケール要件
- Decision: JWT/Bearer認証、PDF一時保存、1PDFあたり100フィールド/10MB上限
- Rationale: API運用の一般的なセキュリティ・パフォーマンス基準
- Alternatives considered: 認証なし、上限なし（リスク高）
