from src.pfag.skills.warning import WarningMessage, get_all_warnings, add_warning, find_warning_by_code

def test_warning_message_fields():
    w = WarningMessage(code="W002", message="msg", description="desc")
    assert w.code == "W002"
    assert w.lang == "ja"

def test_warning_registry():
    w = WarningMessage(code="W003", message="m", description="d")
    add_warning(w)
    found = find_warning_by_code("W003")
    assert found["code"] == "W003"
    all_w = get_all_warnings()
    assert any(x["code"] == "W003" for x in all_w)
