from src.pfag.core.config import config

def test_config_defaults():
    assert config.PORT == 8000
    assert config.DEBUG is True
