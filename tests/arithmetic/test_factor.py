import pytest

from arithmetic.factor import factor


@pytest.mark.parametrize("input_test, expected", [
    (2, [2]),
    (3, [3]),
    (10, [2, 5]),
    (28, [2, 2, 7]),
])
def test_factor(input_test, expected):
    assert factor(input_test) == expected
