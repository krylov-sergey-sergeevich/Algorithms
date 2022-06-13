import pytest

from arithmetic.is_prime import is_prime


@pytest.mark.parametrize("input_test, expected", [
    (3, True),
    (7, True),
    (10e9 + 7, True),
    (10e9 + 8, False),
])
def test_is_prime(input_test, expected):
    assert is_prime(input_test) is expected
