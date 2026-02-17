---

## バージョン情報 / Version Info
- バージョン: 1.0.0
- 最終更新日 / Last updated: 2026-02-17

## 更新履歴 / History
- 2026-02-17: ドキュメント改善（Issue 10）対応、英語併記・Glossary・レビューフロー追加

# フィードバック歓迎 / Feedback Welcome
このドキュメントは非専門家・英語話者を含む多様な利用者のフィードバックを歓迎します。
We welcome feedback from non-experts and English speakers. Please use GitHub Issues or PR comments for any suggestions or questions.


### ドキュメント差分レビュー手順 / Documentation Diff Review Procedure
1. PR作成時、必ず関連ドキュメントの差分を含める
2. PR説明欄に「どのドキュメントをどの理由で更新したか」を明記
3. レビュワーは「レビューテンプレート」に沿って、差分・用語・整合性・表記ゆれを確認
4. 指摘・修正はPRコメントでやりとりし、必要に応じて追加コミット
5. ドキュメント差分の最終確認後、PRをマージ

---
1. Always include related documentation diffs in your PR.
2. Clearly state in the PR description which documents were updated and why.
3. Reviewers check diffs, terminology, consistency, and expression using the review template.
4. Discuss and address feedback via PR comments; add commits as needed.
5. Merge the PR after final confirmation of documentation diffs.

### 主要な機能・手順変更時の運用例 / When to Update Docs
- コードや仕様の主要な変更時は、必ず関連ドキュメント（README.md, docs/, specs/配下）も同時に修正・更新してください。
- PRには「ドキュメント差分」も含め、レビュワーが内容の最新性・整合性を確認できるようにします。

#### サンプルPRタイトル・説明例 / Sample PR Title & Description
> feat: ユーザー認証機能追加 + ドキュメント更新
> 
> - ユーザー認証API追加（src/pfag/api/auth.py）
> - README.mdにAPI仕様・利用例を追記
> - docs/module-design.mdに認証モジュール設計を追加

#### 差分レビュー・レビューテンプレート活用例 / Diff Review & Template Usage
1. PR作成時、必ず「ドキュメント差分」も含める
2. レビュワーは下記テンプレートで最新性・整合性・表記ゆれ等を確認
3. 指摘・修正はPRコメントでやりとり

**レビューテンプレート / Review Template**
> このPRに関連するドキュメントの内容について、最新性・整合性の観点からレビューをお願いします。
> - 変更点が正しく反映されているかご確認ください。
> - 用語や手順の表記ゆれがないかご指摘ください。
> - コメントはこのPRに直接記載してください。

---
## ドキュメント更新運用ルール / Documentation Update Policy

- 主要な機能・手順の変更ごとに、必ず該当するdocs/・README.md・specs/配下のドキュメントを同時に更新してください。
- PR作成時は、ドキュメント差分も必ず含め、レビュワーが内容の最新性・整合性を確認できるようにしてください。
- ドキュメント更新依頼・レビューはGitHub IssueまたはPRコメントで行い、依頼テンプレート例を活用してください。

**依頼テンプレート例 / Request Template Example**
> このPRに関連するドキュメントの内容について、最新性・整合性の観点からレビューをお願いします。
> - 変更点が正しく反映されているかご確認ください。
> - 用語や手順の表記ゆれがないかご指摘ください。
> - コメントはこのPRに直接記載してください。

# PFAG FastAPI APIサーバー Quickstart / PFAG FastAPI API Server Quickstart

## 概要 / Overview
PFAGはPDFフォーム自動生成・解析のためのFastAPIサーバーです。
PFAG is a FastAPI server for automatic PDF form generation and analysis.

## 必要条件 / Requirements
- Python 3.8以上 / Python 3.8 or higher
- pipで依存パッケージインストール可能 / pip installable dependencies

## セットアップ手順 / Setup Steps
### 新規ユーザー検証フィードバック / New User Feedback

- セットアップ手順は明確で、依存パッケージのインストール・サーバー起動・疎通確認まで迷わず実行可能でした。
- "pip install -r requirements.txt" でエラーが出た場合はPythonバージョンや仮想環境の確認を追記すると親切です。
- "uvicorn"コマンドが見つからない場合は "pip install uvicorn" を明記するとより親切です。

#### 追加推奨事項 / Additional Recommendations
- Python仮想環境の作成例を追記（例: python -m venv .venv）
- Windows/Mac/Linuxのコマンド例も併記するとさらに親切

1. 依存パッケージのインストール / Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
2. サーバー起動 / Start server
   ```sh
   uvicorn src.pfag.api.main:app --reload
   ```
3. 疎通確認 / Health check
   - ブラウザまたはcurlで http://localhost:8000/health にアクセス
   - Access http://localhost:8000/health via browser or curl
   - `{ "status": "ok" }` が返れば成功 / If you get `{ "status": "ok" }`, it's working

## トラブルシューティング / Troubleshooting
- ポート競合: `uvicorn`起動時にエラーが出た場合、`--port`オプションで空きポートを指定
   - Port conflict: If you get an error on `uvicorn` startup, specify a free port with `--port` option
- 依存不足: `ModuleNotFoundError`等が出た場合、`pip install -r requirements.txt`を再実行
   - Missing dependencies: If you see `ModuleNotFoundError`, rerun `pip install -r requirements.txt`


## 開発Tips / Development Tips
- APIドキュメント: http://localhost:8000/docs
- API docs: http://localhost:8000/docs
- テスト: `pytest`で自動化（tests/contract, tests/integration）
- Automated tests: Use `pytest` (see tests/contract, tests/integration)
- テスト実行例: `pytest tests/` を実行すると全テストが走ります。
- Example: Run all tests with `pytest tests/`.

---


## 表記ゆれ防止ガイドライン / Consistency Guidelines
- ファイル名・モジュール名は英数字・ハイフンのみ / Use only alphanumeric and hyphens for file/module names
- 用語はGlossaryに登録し、docs/・specs/で統一 / Register all terms in the Glossary and use consistently in docs/specs
- 日本語・英語併記を推奨 / Use both Japanese and English where possible
- ファイル名・モジュール名は一意で重複禁止 / File/module names must be unique
- 本ガイドラインは全ドキュメント・コードに適用されます。
- These guidelines apply to all documentation and code.

---



## 用語集 / Glossary
Glossary of key terms used in this project. 日本語・英語併記で主要用語を解説します。

| 用語 (JP)         | Term (EN)         | 説明 / Description |
|-------------------|-------------------|--------------------|
| セットアップ       | Setup             | 環境構築手順 / Environment setup steps |
| 疎通確認           | Health check       | サーバーが正常に動作しているかの確認 / Server health verification |
| 依存パッケージ     | Dependencies       | 必要なPythonパッケージ / Required Python packages |
| APIドキュメント     | API docs           | OpenAPI仕様の自動生成ドキュメント / Auto-generated OpenAPI docs |
| 表記ゆれ           | Consistency        | 用語・表現の不統一 / Inconsistent terms or expressions |
| 一意性             | Uniqueness         | 名前や識別子が重複しないこと / No duplicate names or identifiers |
| モジュール         | Module             | システムの機能単位 / Functional unit of the system |
| 責務               | Responsibility     | モジュールが担う役割 / Role of the module |
| 差分レビュー       | Diff review        | ドキュメントやコードの変更点を確認する作業 / Reviewing changes in docs or code |
| テンプレート       | Template           | 定型的な記載例 / Standardized example or format |
| Glossary           | Glossary           | 用語集 / List of terms |
