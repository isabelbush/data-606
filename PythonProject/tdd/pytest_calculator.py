import pytest

from calculator import add

@pytest.mark.parametrize('num1, num2, expected_result', [
    (2, 1, 1),
    (10, 5, 5),
    (20, 10, 10)
])

def test_subtract(num1, num2, expected_result):
    assert add(2, 1) == 3