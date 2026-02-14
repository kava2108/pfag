# Data Model: 下線検出（テキストフィールド）

## Entities

### Underline
- id: str (unique)
- image_id: str
- start_x: int
- start_y: int
- end_x: int
- end_y: int
- width: int
- thickness: int

### BoundingBox
- id: str (unique)
- underline_id: str
- x: int (left)
- y: int (top)
- width: int
- height: int

### FieldLayoutRule
- id: str (unique)
- bounding_box_id: str
- height: int (default: 20)
- offset: int (default: 5)
- inset: int (default: 2)

## Relationships
- Underline 1:N BoundingBox
- BoundingBox 1:1 FieldLayoutRule

## Validation Rules
- width >= 30px
- thickness >= 2px
- bounding box width >= underline width
- bounding box height >= 20px
- offset, inset >= 0

## State Transitions
- [uploaded] → [detected] → [boxed] → [layout_applied]
