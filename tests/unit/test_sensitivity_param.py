from src.pfag.skills.sensitivity import SensitivityParam
import pytest

def test_sensitivity_param_adjust():
    param = SensitivityParam(param_name="thresh", value=0.5, min_value=0.0, max_value=1.0, default=0.5, description="test")
    param.adjust(0.8)
    assert param.value == 0.8
    with pytest.raises(ValueError):
        param.adjust(2.0)
