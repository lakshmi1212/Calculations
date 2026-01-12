import sys
sys.path.insert(0, './src')
from math_operations import add
import pytest

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 0) == 0

def test_add_mixed():
    assert add(-2, 3) == 1

def test_add_float():
    assert add(2.5, 3.1) == pytest.approx(5.6)

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
