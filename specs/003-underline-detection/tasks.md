# Tasks: 下線検出（テキストフィールド）

## Phase 2: Implementation Tasks

### 設計・基盤
- [ ] T001: src/pfag/core/underline_detection.py 新規作成（サービス本体スケルトン）
- [ ] T002: src/pfag/cli/underline_detect.py 新規作成（CLIスケルトン）
- [ ] T003: API仕様（contracts/openapi.yaml）に基づくエンドポイント設計

### 画像処理・下線検出
- [ ] T010: OpenCVによる画像前処理（グレースケール・二値化・ノイズ除去）
- [ ] T011: モルフォロジー演算による水平線強調処理
- [ ] T012: Hough変換による水平直線抽出
- [ ] T013: min_line_width, line_gap_threshold, thickness, lengthパラメータ適用
- [ ] T014: 誤検出抑制（最小幅・長さ・太さ閾値）
- [ ] T015: 下線情報（座標・幅・太さ）抽出

### バウンディングボックス・配置ルール
- [ ] T020: バウンディングボックス生成ロジック実装
- [ ] T021: フィールド配置ルール（高さ・オフセット・インセット）適用

### API/CLI/プレビュー
- [ ] T030: /underline/detect API実装
- [ ] T031: /underline/preview API実装（下線付き画像返却）
- [x] T032: CLI引数・出力整備

### テスト・ドキュメント
- [x] T040: 単体テスト（tests/unit/test_underline_detection.py）作成
- [x] T041: コントラクトテスト（tests/contract/test_underline_detection.py）作成
- [x] T042: サンプル画像・PDF生成スクリプト作成
- [x] T043: quickstart.md・API仕様・設計ドキュメント整備

### Polish・最終確認
- [x] T050: パフォーマンス・メモリ・バリデーション最適化
- [x] T051: ログ出力・エラーハンドリング強化
- [x] T052: コード・テスト・ドキュメント最終レビュー
