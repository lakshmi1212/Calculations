import pytest
from src.math_operations import subtract


def test_subtract_positive():
    assert subtract(5, 3) == 2


def test_subtract_negative():
    assert subtract(-1, -2) == 1


def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5


def test_subtract_float():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)


def test_subtract_large_numbers():
    assert subtract(1000000, 999999) == 1
