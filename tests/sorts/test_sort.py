import pytest

from sorts.selection_sort import selection_sort
from sorts.insertion_sort import insertion_sort
from sorts.bubble_sort import bubble_sort
from sorts.merge_sort import merge_sort
from sorts.quick_sort import quick_sort
from sorts.count_sort import count_sort


@pytest.mark.parametrize("input_test, expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([3, -1, 0, 2, 7, 5], [-1, 0, 2, 3, 5, 7]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
    ([2, 3, 4, 5, 6, 1], [1, 2, 3, 4, 5, 6]),
])
def test_selection_sort(input_test, expected):
    assert selection_sort(input_test) == expected
    assert insertion_sort(input_test) == expected
    assert bubble_sort(input_test) == expected


@pytest.mark.parametrize("input_test, expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([3, -1, 0, 2, 7, 5], [-1, 0, 2, 3, 5, 7]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
    ([2, 3, 4, 5, 6, 1], [1, 2, 3, 4, 5, 6]),
])
def test_insertion_sort(input_test, expected):
    assert insertion_sort(input_test) == expected


@pytest.mark.parametrize("input_test, expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([3, -1, 0, 2, 7, 5], [-1, 0, 2, 3, 5, 7]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
    ([2, 3, 4, 5, 6, 1], [1, 2, 3, 4, 5, 6]),
])
def test_bubble_sort(input_test, expected):
    assert bubble_sort(input_test) == expected


@pytest.mark.parametrize("input_test, expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([3, -1, 0, 2, 7, 5], [-1, 0, 2, 3, 5, 7]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
    ([2, 3, 4, 5, 6, 1], [1, 2, 3, 4, 5, 6]),
])
def test_merge_sort(input_test, expected):
    assert merge_sort(input_test) == expected


@pytest.mark.parametrize("input_test, expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([3, -1, 0, 2, 7, 5], [-1, 0, 2, 3, 5, 7]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
    ([2, 3, 4, 5, 6, 1], [1, 2, 3, 4, 5, 6]),
])
def test_quick_sort(input_test, expected):
    assert quick_sort(input_test) == expected


@pytest.mark.parametrize("input_test, expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
    ([2, 3, 4, 5, 6, 1], [1, 2, 3, 4, 5, 6]),
])
def test_count_sort(input_test, expected):
    assert count_sort(input_test) == expected
