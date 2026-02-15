# Feature Specification: [FEATURE NAME]

# Feature Specification: 座標変換（画像座標 → PDF座標）

**Feature Branch**: `005-coordinate-conversion`
**Created**: 2026-02-15
**Status**: Draft
**Input**: User description: "座標変換（画像座標 → PDF座標）\n- PDF サイズ（pt）と画像サイズ（px）を取得する処理を実装\n- X 座標変換式を実装\n  X_pdf = X_img * (Width_pdf / Width_img)\n- Y 座標変換式を実装\n  Y_pdf = Height_pdf - (Y_img * (Height_pdf / Height_img))\n- アスペクト比差異の検証\n- 単体テスト：座標変換の誤差が許容範囲内であることを確認"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - 座標変換結果の取得 (Priority: P1)

ユーザーは画像上の座標をPDF座標に正確に変換できる。

**Why this priority**: PDF上で正確な位置指定が必要なため、変換精度が最重要。

**Independent Test**: サンプル画像とPDFで座標変換を行い、変換結果が期待値と一致するか検証できる。

**Acceptance Scenarios**:

1. **Given** 画像サイズとPDFサイズが取得できている, **When** 画像座標を入力, **Then** PDF座標が正しく返される
2. **Given** アスペクト比が異なる場合, **When** 座標変換を実施, **Then** 誤差が許容範囲内である

---

### User Story 2 - アスペクト比差異の検証 (Priority: P2)

ユーザーは画像とPDFのアスペクト比差異による変換誤差を確認できる。

**Why this priority**: アスペクト比の違いによる誤差が業務上問題となる場合があるため。

**Independent Test**: アスペクト比が異なる画像・PDFで変換誤差を計測し、許容範囲内か確認できる。

**Acceptance Scenarios**:

1. **Given** アスペクト比が異なる画像とPDF, **When** 座標変換を実施, **Then** 誤差が計測される

---

### User Story 3 - 単体テストによる検証 (Priority: P3)

開発者は座標変換ロジックの単体テストを実施し、誤差が許容範囲内であることを確認できる。

**Why this priority**: 品質保証のため、テストによる検証が必要。

**Independent Test**: テストケースで座標変換結果の誤差を計測し、許容範囲内か確認できる。

**Acceptance Scenarios**:

1. **Given** テスト用画像・PDFサイズと座標, **When** 座標変換を実施, **Then** 誤差が許容範囲内である

---

### Edge Cases

- 画像サイズまたはPDFサイズが0の場合はどうなるか？
- アスペクト比が極端に異なる場合の誤差は？
- 入力座標が画像範囲外の場合の挙動は？

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: システムは画像サイズ（px）とPDFサイズ（pt）を取得できなければならない
- **FR-002**: システムはX座標変換式 `X_pdf = X_img * (Width_pdf / Width_img)` を適用できなければならない
- **FR-003**: システムはY座標変換式 `Y_pdf = Height_pdf - (Y_img * (Height_pdf / Height_img))` を適用できなければならない
- **FR-004**: システムはアスペクト比差異による変換誤差を検証できなければならない
- **FR-005**: システムは座標変換の誤差が許容範囲内であることを単体テストで確認できなければならない
- **FR-006**: システムは座標変換後の誤差許容範囲を±2ptとしなければならない（理由：画像座標 → PDF座標変換におけるDPI換算・丸め誤差を考慮し、帳票実務上の許容範囲（約±0.7mm）と整合するため）

### Key Entities

- **画像サイズ**: 幅（px）、高さ（px）
- **PDFサイズ**: 幅（pt）、高さ（pt）
- **座標**: 画像座標（X_img, Y_img）、PDF座標（X_pdf, Y_pdf）
- **変換誤差**: 計算結果と期待値との差

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: ユーザーが画像座標からPDF座標への変換を1秒以内で完了できる
- **SC-002**: アスペクト比差異による変換誤差が許容範囲内である
- **SC-003**: 単体テストで全ての変換ケースが許容誤差内で合格する
- **SC-004**: ユーザーから座標変換精度に関する問い合わせが30%減少する
- **FR-001**: System MUST [specific capability, e.g., "allow users to create accounts"]
