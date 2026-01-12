import sys
sys.path.insert(0, './src')
from math_operations import subtract
import pytest

def test_subtract_positive():
    assert subtract(5, 3) == 2

def test_subtract_negative():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(0, 0) == 0

def test_subtract_mixed():
    assert subtract(-5, 3) == -8

def test_subtract_float():
    assert subtract(5.5, 3.1) == pytest.approx(2.4)

def test_subtract_large_numbers():
    assert subtract(3000000, 1000000) == 2000000
