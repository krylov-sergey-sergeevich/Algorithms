import pytest

from search.binary_search import binary_search


@pytest.mark.parametrize("input_test, expected", [
    ([2, 3, 3, 5, 8, 8, 9, 10, 12], False),
    ([2, 3, 3, 5, 7, 8, 9, 10, 12], True),
    ([2, 3, 3, 5, 6, 8, 9, 10, 12], False),
])
def test_selection_sort(input_test, expected):
    assert binary_search(input_test, 7) == expected
