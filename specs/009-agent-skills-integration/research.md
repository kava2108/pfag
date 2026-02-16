# Phase 0: Research (Agent Skills連携機能)

## 技術的な不明点・調査事項

- スキルスキーマの記述・保存方式（JSON Schema/Pydantic/独自？）
- APIラッパの設計パターン（同期/非同期、例外処理、型安全性）
- 感度調整ロジックの設計（パラメータ範囲・バリデーション・UI連携）
- 警告説明の多言語対応・テンプレート化の有無
- テスト戦略（contract/integration/unitの分担、モック方針）

## 依存技術・ベストプラクティス調査

- Pydanticによるスキーマ定義・バリデーションのベストプラクティス
- FastAPIでのAPIラッパ設計パターン
- Pythonでの感度調整パラメータ設計例
- ユーザー向け警告説明の設計パターン
- pytestによるテスト分離・モック戦略

## 参考文献・リンク
- [Pydantic公式](https://docs.pydantic.dev/)
- [FastAPI公式](https://fastapi.tiangolo.com/)
- [pytest公式](https://docs.pytest.org/)

---

**この内容をもとにPhase 1: data-model, contracts, quickstartを設計します。**
