from pydantic import BaseModel, Field
from typing import Union


class SensitivityParam(BaseModel):
    """感度調整パラメータモデル"""
    param_name: str = Field(..., description="パラメータ名")
    value: Union[float, int] = Field(..., description="現在値")
    min_value: Union[float, int] = Field(..., description="最小値")
    max_value: Union[float, int] = Field(..., description="最大値")
    default: Union[float, int] = Field(..., description="デフォルト値")
    description: str = Field(..., description="説明")

    def adjust(self, new_value: Union[float, int]) -> None:
        """感度パラメータを調整（バリデーション付き）"""
        if not (self.min_value <= new_value <= self.max_value):
            raise ValueError(f"{self.param_name} must be between {self.min_value} and {self.max_value}")
        self.value = new_value
