import pytest

from dp.gis import gis, gis_fast


@pytest.mark.parametrize("input_test, expected", [
    ([2, 7, 1, 4, 3, 5, 4, 6, 2, 5, 8, 3], [2, 4, 5, 6, 8]),
])
def test_gis(input_test, expected):
    assert gis(input_test) == expected


@pytest.mark.parametrize("input_test, expected", [
    ([2, 7, 1, 4, 3, 5, 4, 6, 2, 5, 8, 3], 5),
    ([1], 1),
    ([3, 2, 1], 1),
    ([1, 2, 3], 3),
])
def test_gis_fast(input_test, expected):
    assert gis_fast(input_test) == expected
