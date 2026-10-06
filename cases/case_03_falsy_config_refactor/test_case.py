import pytest

from cases.case_03_falsy_config_refactor import buggy, fixed


DEFAULTS = {
    "retry_count": 3,
    "enabled": True,
    "label": "default",
}

USER = {
    "retry_count": 0,
    "enabled": False,
    "label": "",
}

EXPECTED = {
    "retry_count": 0,
    "enabled": False,
    "label": "",
}


@pytest.mark.xfail(
    strict=True,
    reason="buggy refactor confuses explicit falsy values with missing values",
)
def test_buggy_preserves_explicit_falsy_values():
    assert buggy.effective_settings(DEFAULTS, USER) == EXPECTED


def test_fixed_preserves_explicit_falsy_values():
    assert fixed.effective_settings(DEFAULTS, USER) == EXPECTED


def test_fixed_uses_default_only_when_key_is_missing():
    result = fixed.effective_settings(DEFAULTS, {"enabled": False})

    assert result == {
        "retry_count": 3,
        "enabled": False,
        "label": "default",
    }
