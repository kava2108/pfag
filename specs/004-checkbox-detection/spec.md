
# Feature Specification: チェックボックス検出（矩形検出）

**Feature Branch**: `004-checkbox-detection`  
**Created**: 2026-02-14  
**Status**: Draft  
**Input**: User description: "チェックボックス検出（矩形検出）を実装する。画像またはPDFから手書き・印刷のチェックボックス（四角形）を検出し、その座標・サイズ・塗りつぶし状態（ON/OFF）を返す。主な用途は帳票やアンケートの自動読取。水平・垂直に近い矩形のみ対象、ノイズや非矩形は除外。API・CLI・テスト・サンプル画像も含む。"

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.
  
  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->


### User Story 1 - 帳票画像からチェックボックスを検出 (Priority: P1)

帳票やアンケートのスキャン画像/PDFをアップロードすると、システムが手書き・印刷のチェックボックス（四角形）を自動検出し、各チェックボックスの座標・サイズ・塗りつぶし状態（ON/OFF）を返す。

**Why this priority**: 自動読取の主目的であり、最も重要なユースケース。

**Independent Test**: サンプル帳票画像をAPI/CLIに投入し、正しい矩形座標・ON/OFF判定が返ることを確認。

**Acceptance Scenarios**:
1. **Given** 画像/PDFに複数のチェックボックスが含まれる, **When** API/CLIで検出を実行, **Then** すべてのチェックボックスの座標・サイズ・ON/OFFが返る
2. **Given** チェックが入っていないボックス, **When** 検出, **Then** ON/OFFが正しくOFFと判定される
3. **Given** チェックが塗りつぶされたボックス, **When** 検出, **Then** ON/OFFが正しくONと判定される

---

### User Story 2 - ノイズ・非矩形の除外 (Priority: P2)

画像内のノイズや手書きの非矩形、線が途切れた枠などはチェックボックスとして誤検出されない。

**Why this priority**: 実運用での誤検出防止・信頼性向上のため。

**Independent Test**: ノイズや非矩形を含む画像で誤検出がないことを確認。

**Acceptance Scenarios**:
1. **Given** ノイズや非矩形が含まれる画像, **When** 検出, **Then** チェックボックス以外は返されない

---

### User Story 3 - サンプル画像・テスト容易性 (Priority: P3)

サンプル画像やテスト用PDFを用意し、CLI/API/テストで再現性のある検証ができる。

**Why this priority**: 品質担保・CI/CD自動化のため。

**Independent Test**: サンプル画像での自動テストが通ること。

**Acceptance Scenarios**:
1. **Given** サンプル画像, **When** テスト実行, **Then** 期待通りの検出結果が得られる

---

### Edge Cases

- チェックボックスが画像端に接している場合はどう扱うか？
- 枠線が一部欠けている場合の判定は？
- 非常に小さい/大きい矩形（閾値外）は除外されるか？
- 塗りつぶしが薄い・斜め線などON/OFF判定が曖昧な場合の扱いは？
- 回転・傾きがある場合の検出精度は？

## Requirements *(mandatory)*

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right functional requirements.
-->


### Functional Requirements

- **FR-001**: システムは画像またはPDFから矩形（チェックボックス）を検出できること
- **FR-002**: 検出した各チェックボックスの座標（x, y）、サイズ（幅・高さ）を返すこと
- **FR-003**: 各チェックボックスの塗りつぶし状態（ON/OFF）を判定し返すこと
- **FR-004**: 水平・垂直に近い矩形のみを対象とし、ノイズや非矩形は除外すること
- **FR-005**: API・CLI両方で同等の検出・出力ができること
- **FR-006**: サンプル画像・テストデータを用意し、再現性のあるテストが可能であること
- **FR-007**: 入力画像サイズや矩形サイズの閾値をパラメータで調整できること
- **FR-008**: 検出結果はJSON形式で返すこと
- **FR-009**: エラー時は適切なエラーメッセージを返すこと


### Key Entities

- **CheckBox**: 検出されたチェックボックス。属性: x, y, width, height, is_checked (ON/OFF)

## Success Criteria *(mandatory)*

<!--
  ACTION REQUIRED: Define measurable success criteria.
  These must be technology-agnostic and measurable.
-->


### Measurable Outcomes

- **SC-001**: 95%以上のチェックボックスが正しく検出・ON/OFF判定される
- **SC-002**: ノイズ・非矩形の誤検出率が5%未満である
- **SC-003**: サンプル画像・PDFで全ケースが自動テストで合格する
- **SC-004**: 画像1枚あたりの検出処理が3秒以内で完了する
