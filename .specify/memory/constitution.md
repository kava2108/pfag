# PFAG Constitution


## Core Principles

### I. Library-First
- すべての機能は独立したライブラリとして設計・実装すること
- ライブラリは自己完結・独立テスト・ドキュメント必須
- 組織都合のみのライブラリは禁止

### II. CLI & API Interface
- すべてのライブラリはCLIまたはAPI経由で機能を公開すること
- 入出力はテキスト（stdin/args→stdout, エラーはstderr）
- JSONおよび人間可読形式をサポート

### III. Test-First (NON-NEGOTIABLE)
- TDD必須：テスト→ユーザー承認→テスト失敗→実装
- Red-Green-Refactorサイクル厳守

### IV. Integration Testing
- 新規ライブラリ・契約変更・サービス間通信・共通スキーマは必ず統合テストを実施

### V. Observability & Versioning
- テキストI/Oでデバッグ容易性を担保
- 構造化ログ必須
- バージョンはMAJOR.MINOR.PATCH方式


## Additional Constraints
- Python 3.8以上、FastAPI, OpenCV, PyMuPDF, pdfrw/PyPDF2を推奨
- セキュリティ: 一時ファイルは即時削除、外部入力はバリデーション必須
- ドキュメント・API仕様は常に最新を維持


## Development Workflow
- すべてのPRはconstitution遵守をレビューチェック
- テスト・ドキュメント・型アノテーション必須
- 複雑化は正当な理由がある場合のみ許容
- 仕様・設計・実装・テスト・デプロイの各段階で合意形成


## Governance
- 本constitutionは他の全ての開発慣行に優先
- 改訂には文書化・承認・移行計画が必要
- すべてのPR/レビューで遵守確認
- 複雑性は必ず正当化
- ランタイム開発ガイダンスはREADME.mdを参照

**Version**: 1.0.0 | **Ratified**: 2026-02-16 | **Last Amended**: 2026-02-16
