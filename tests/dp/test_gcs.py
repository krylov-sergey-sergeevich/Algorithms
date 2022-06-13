import pytest

from dp.gcs import gcs


@pytest.mark.parametrize("input_test, expected", [
    (("baccbca", "abcabaac"), (4, "abcb")),
])
def test_gcs(input_test, expected):
    assert gcs(input_test[0], input_test[1]) == expected
