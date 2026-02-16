# research.md: formify API integration test

## Decision: Python 3.12, FastAPI, pytest, python-multipart
- Rationale: プロジェクト標準・既存実装と統一。CI/CD・ローカル両対応。
- Alternatives considered: 他のWebフレームワーク（Flask, Django）、他のテストフレームワーク（unittest, nose）

## Decision: 非機能要件（パフォーマンス・スケーラビリティ等）はスコープ外
- Rationale: 本APIはCI/CD自動テスト用であり、性能・可用性・セキュリティ要件は仕様外とすることで設計・テストの誤解を防ぐ
- Alternatives considered: レスポンスタイム上限や負荷試験を追加する案もあったが、現状不要

## Decision: テストはpytest+TestClientで自動化
- Rationale: FastAPI公式推奨、既存テスト資産との親和性
- Alternatives considered: curlやhttpxによる外部E2Eも検討したが、単体APIテストはTestClientで十分

## Decision: 検出処理はダミー実装（常に0件）
- Rationale: 本APIの主目的はI/O・バリデーション・レスポンス仕様の検証であり、検出ロジック自体は本件スコープ外
- Alternatives considered: モックやfixtureで検出件数を制御する案もあったが、現状は常に0件で十分

## Decision: PDFバイナリはダミーで十分
- Rationale: バリデーション・レスポンス検証が主目的のため、実際のPDF内容は問わない
- Alternatives considered: 実PDF生成やサンプルファイル利用も可能だが、テスト簡素化を優先

## Decision: 仕様・テストはspecs/008-formify-api-integration-test/配下で管理
- Rationale: speckit標準構成・他機能との一貫性
- Alternatives considered: tests/配下にまとめる案もあったが、ドキュメント分離を優先
