# Data Model: チェックボックス検出

## Entity: CheckBox
- x: int
- y: int
- width: int
- height: int
- is_checked: bool

## 検出結果（JSON例）
```
{
  "checkboxes": [
    {"x": 100, "y": 200, "width": 20, "height": 20, "is_checked": true},
    {"x": 300, "y": 400, "width": 22, "height": 22, "is_checked": false}
  ]
}
```
