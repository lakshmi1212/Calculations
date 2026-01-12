import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-2, -4) == -6

def test_add_mixed_sign_numbers():
    assert add(-7, 10) == 3

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(7, 0) == 7

def test_add_large_numbers():
    assert add(1_000_000, 2_000_000) == 3_000_000
