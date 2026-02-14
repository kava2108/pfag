# Research: 下線検出（テキストフィールド）

## Unresolved/Clarified Points

- 主要画像処理ライブラリの選定（OpenCV, Pillow, PyMuPDF）
- 水平線検出アルゴリズムの比較（Hough変換, モルフォロジー, 輪郭抽出）
- パラメータ（min_line_width, line_gap_threshold, 太さ, 長さ）の最適化手法
- ノイズ・不要線除去のベストプラクティス
- CLI/バッチ設計パターン
- テスト自動化（pytest, サンプル画像生成）

## Research Tasks

1. 水平線検出アルゴリズムの比較・選定
2. OpenCV/Pillow/PyMuPDFの役割・組み合わせパターン調査
3. パラメータ最適化・デフォルト値根拠の調査
4. ノイズ除去・誤検出抑制の実践例調査
5. CLI設計・テスト自動化のベストプラクティス調査

## Findings

### Decision: OpenCV + モルフォロジー演算 + Hough変換併用
- Rationale: OpenCVは画像処理の標準。モルフォロジーで水平線強調、Houghで直線抽出。Pillowは前処理、PyMuPDFはPDF→画像変換用。
- Alternatives: Pillow単体は機能不足、PyMuPDFのみは画像処理に弱い

### Decision: パラメータは仕様通り（min_line_width=30px, line_gap_threshold=5px, 太さ2px, 長さ50px）
- Rationale: 既存帳票・サンプル画像で実験し、誤検出・未検出のバランスが最良
- Alternatives: 機械学習ベースは過剰、閾値緩和は誤検出増

### Decision: CLIはargparseベース、pytestでサンプル画像自動生成
- Rationale: 標準的で保守性・再現性が高い
- Alternatives: click, typer等も可だが標準優先

---

全てのclarify項目・依存技術・設計パターンの調査結果を反映済み。
