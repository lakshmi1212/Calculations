import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2
    assert subtract(200, 100) == 100

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2
    assert subtract(-100, 50) == -150

def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(0, 5) == -5
    assert subtract(7, 0) == 7

def test_subtract_floats():
    assert subtract(5.5, 3.1) == pytest.approx(2.4)
    assert subtract(-1.1, 1.1) == pytest.approx(-2.2)

def test_subtract_large_numbers():
    assert subtract(3_000_000_000, 1_000_000_000) == 2_000_000_000
