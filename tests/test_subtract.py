import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (-1, -2, 1),
    (0, 0, 0),
    (5.5, 2.5, 3.0),
    (1, -1, 2),
    (1000000, 500000, 500000)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
