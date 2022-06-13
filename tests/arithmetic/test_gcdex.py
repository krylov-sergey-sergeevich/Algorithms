import pytest

from arithmetic.gcdex import gcdex, gcdex_print


@pytest.mark.parametrize("input_test, expected", [
    ((2, 10), (2, 1, 0)),
])
def test_gcdex(input_test, expected):
    # (d, x, y) таких что где d = НОД(a, b), a*x+b*y = d
    assert gcdex(*input_test) == expected


def test_gcdex_print(capture_stdout):
    # (d, x, y) таких что где d = НОД(a, b), a*x+b*y = d
    gcdex_print(2, 10)
    assert str.__contains__(capture_stdout["stdout"], "2 * 1 + 10 * 0 = 2")
