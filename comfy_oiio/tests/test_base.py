import pytest


def test_human_readable():
    """Various test case for the humand readable function."""
    assert True is True


def test_example_float_approx():
    assert pytest.approx(0.3) == 0.1 + 0.2


def test_example_error():
    with pytest.raises(ValueError):
        int("string")
