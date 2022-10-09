import pytest

from arithmetic.gcd import gcd, gcd_recursion


def test_gcd():
    assert gcd(10, 2) == 2
    assert gcd_recursion(10, 2) == 2


@pytest.mark.parametrize("input_test, expected", [
    ((3, 7), 1),
    ((3, 7), 1),
    ((0, 1), 1)
])
def test_gcd_prime_numbers(input_test, expected):
    assert gcd(*input_test) is expected
    assert gcd_recursion(*input_test) is expected


@pytest.mark.skip(reason="Not implemented")
def test_gcd_exception_by_zero():
    assert gcd(0, 0) == 0
    assert gcd_recursion(0, 0) == 0


@pytest.mark.xfail
def test_gcd_zero():
    assert gcd(0, 0) == 0
    assert gcd_recursion(0, 0) == 0
