# Phase 0: research.md

## Decision: FastAPI + uvicorn でAPIサーバー初期化
- FastAPIはPython製の軽量Web APIフレームワークであり、開発効率・拡張性・型安全性に優れる。
- uvicornはFastAPI公式推奨のASGIサーバーで、開発・本番どちらでも利用可能。

## Rationale
- PythonプロジェクトでAPIサーバーを最速で立ち上げるにはFastAPIが最適。
- ドキュメント自動生成（/docs）や型ヒント活用、非同期対応など現代的な要件を満たす。
- uvicornはFastAPIと組み合わせて使うことで、開発時のホットリロードや本番運用も容易。

## Alternatives considered
- Flask: シンプルだが型安全性や自動ドキュメント生成が弱い。
- Django: フルスタックだが初期化・学習コストが高い。
- Starlette: FastAPIの下位互換であり、API設計にはFastAPIがより適切。

## /healthエンドポイント設計
- JSONで { "status": "ok" } を返す。
- 機械可読性・拡張性の観点からプレーンテキストより推奨。

## 依存パッケージ
- fastapi
- uvicorn
- pytest（テスト用、Phase 1で詳細設計）

## 参考
- https://fastapi.tiangolo.com/
- https://www.uvicorn.org/
