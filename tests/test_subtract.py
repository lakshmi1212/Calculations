import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-3, -2) == -1

def test_subtract_mixed_sign_numbers():
    assert subtract(5, -2) == 7
    assert subtract(-5, 2) == -7

def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
