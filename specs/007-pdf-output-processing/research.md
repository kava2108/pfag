# Research: PDF出力処理（生成フィールドのPDF書き込み・一時ファイル削除・バイナリ返却）

## Decision 1: AcroFormフィールド埋め込み手法
- **Decision**: PyPDF2を用いてJSON形式のフィールド情報を既存PDFへ埋め込む
- **Rationale**: PyPDF2はAcroForm編集に対応し、依存追加コストが低い。JSONはAPI連携・テスト容易。
- **Alternatives considered**: pdfrw（日本語PDFで不安定な場合あり）、pikepdf（AcroForm操作がやや煩雑）

## Decision 2: 一時ファイル管理
- **Decision**: tempfile.TemporaryDirectory/NamedTemporaryFileを利用し、PDF生成・編集時の一時ファイルを管理
- **Rationale**: OS標準・自動削除・セキュリティ担保
- **Alternatives considered**: 独自ディレクトリ管理（削除漏れリスク高）

## Decision 3: バイナリ返却方式
- **Decision**: FastAPIのResponse(content=..., media_type="application/pdf")でバイナリ返却
- **Rationale**: FastAPI標準、クライアント側でのダウンロード・プレビューが容易
- **Alternatives considered**: ファイルパス返却（セキュリティ・一時ファイル競合リスク）

## Decision 4: テスト戦略
- **Decision**: pytestでunit/contract/integrationテストを分離実施
- **Rationale**: 機能単位・API単位・E2Eで品質担保
- **Alternatives considered**: unittestのみ（API/統合テストが煩雑）

## Decision 5: エラー・例外処理
- **Decision**: FastAPIのHTTPExceptionでAPIエラーを一元管理。内部処理はtry/exceptで詳細ログ化
- **Rationale**: クライアントに明確なエラー通知、デバッグ容易
- **Alternatives considered**: 独自例外クラス（FastAPI連携が煩雑）
