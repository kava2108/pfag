# Tasks: チェックボックス検出（矩形検出）

**Input**: Design documents from `/specs/004-checkbox-detection/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

## Phase 1: Setup (Shared Infrastructure)

- [x] T001 プロジェクト構造作成（src/pfag/core, cli, api, tests/unit, contract, sample）
- [x] T002 Python依存パッケージ(OpenCV, NumPy, PyMuPDF, Pillow, FastAPI, pytest)インストール
- [x] T003 [P] Lint/formatツール設定（black, isort, flake8）

---

## Phase 2: Foundational (Blocking Prerequisites)

- [x] T004 サービス本体スケルトン作成（src/pfag/core/checkbox_detection.py）
- [ ] T005 CLIスケルトン作成（src/pfag/cli/checkbox_detect.py）
- [ ] T006 APIエンドポイント設計（src/pfag/api/checkbox.py, contracts/openapi.yaml）
- [x] T007 テストディレクトリ・サンプル生成スクリプト雛形作成

---

## Phase 3: User Story 1 - 帳票画像からチェックボックスを検出 (Priority: P1) 🎯 MVP

**Goal**: 画像/PDFからチェックボックス（四角形）を検出し、座標・サイズ・ON/OFFを返す
**Independent Test**: サンプル帳票画像で正しい検出・ON/OFF判定が返る

- [x] T010 [P] [US1] 単体テスト作成（tests/unit/test_checkbox_detection.py）
- [x] T011 [P] [US1] コントラクトテスト作成（tests/contract/test_checkbox_detection.py）
- [x] T012 [P] [US1] サンプル画像生成スクリプト作成（tests/sample/generate_checkbox_images.py）
- [x] T013 [US1] 画像前処理（グレースケール・二値化・ノイズ除去）実装
	- [x] T014 [US1] 輪郭検出・矩形近似ロジック実装
	- [x] T015 [US1] 塗りつぶし判定（黒画素率計算）実装
	- [x] T016 [US1] 検出結果JSON出力・バリデーション
	- [x] T017 [US1] CLI検出・出力実装
	- [x] T018 [US1] API検出・出力実装
	- [x] T019 [US1] プレビュー画像生成（検出枠描画）

---

## Phase 4: User Story 2 - ノイズ・非矩形の除外 (Priority: P2)

**Goal**: ノイズや非矩形を誤検出しない
**Independent Test**: ノイズ・非矩形画像で誤検出がないこと

	- [x] T020 [P] [US2] ノイズ・非矩形除外ロジック実装（角度・比率・サイズ閾値）
	- [x] T021 [US2] 除外ロジック単体テスト追加
	- [x] T022 [US2] コントラクトテスト追加（ノイズ画像）

---

## Phase 5: User Story 3 - サンプル画像・テスト容易性 (Priority: P3)

**Goal**: サンプル画像・PDFで自動テストが通る
**Independent Test**: サンプル画像での自動テストが合格

	- [x] T030 [P] [US3] サンプル画像・PDF追加
	- [x] T031 [US3] テスト自動化スクリプト追加

---

## Final Phase: Polish & Cross-Cutting

	- [x] T040 パフォーマンス・バリデーション最適化
	- [x] T041 ログ・エラーハンドリング強化
	- [x] T042 コード・テスト・ドキュメント最終レビュー

---

## Dependencies
- US1→US2, US3は独立
- US2はUS1の検出ロジックに依存

## Parallel Execution Examples
- T010, T011, T012は並列可能
- T013〜T015は順次、T017/T018は並列
- US2, US3のテスト系は独立並列

## Implementation Strategy
- MVPはUS1（検出・ON/OFF判定・API/CLI/テスト）
- US2, US3は追加品質・自動化強化
