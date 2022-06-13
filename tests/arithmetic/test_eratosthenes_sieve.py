import pytest

from arithmetic.eratosthenes_sieve import eratosthenes_sieve


@pytest.mark.parametrize("input_test, expected", [
    (1, [True, True]),
    (7, [True, True, True, True, False, True, False, True])
])
def test_eratosthenes_sieve(input_test, expected):
    assert eratosthenes_sieve(input_test) == expected
