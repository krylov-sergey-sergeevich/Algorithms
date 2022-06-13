import pytest

from arithmetic.fibonacci import fib_recursive, fib


@pytest.mark.parametrize("input_test, expected", [
    (20, 6765),
    (10, 55),
    (30, 832040),
])
def test_fib_recursive(input_test, expected):
    assert fib_recursive(input_test) == expected


@pytest.mark.parametrize("input_test, expected", [
    (20, 6765),
    (10, 55),
    (30, 832040),
])
def test_fib(input_test, expected):
    assert fib(input_test) == expected
