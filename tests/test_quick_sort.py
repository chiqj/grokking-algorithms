# coding=utf-8

import pytest

from algorithms.quick_sort import QuickSort, QuickSortInPlace


@pytest.mark.parametrize(
    'array',
    (
        [3, 1, 4, 1, 5, 9, 2, 5, 4],
        [],
        [10],
        [3, 1],
        [1, 2, 2, 3],
    )
)
def test_quick_sort(array):
    obj = QuickSort()
    sorted_array = sorted(array)
    assert obj.sort(array) == sorted_array


@pytest.mark.parametrize(
    'array',
    (
        [3, 1, 4, 1, 5, 9, 2, 5, 4],
        [],
        [10],
        [3, 1],
        [1, 2, 2, 3]
    )
)
def test_quick_sort_in_place(array):
    obj = QuickSortInPlace()
    obj.sort(array)
    assert array == sorted(array)
