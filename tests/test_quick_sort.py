# coding=utf-8

import pytest

from algorithms.quick_sort import QuickSort


@pytest.mark.parametrize('array', ([3, 1, 4, 1, 5, 9], [], [10], [3, 1]))
def test_quick_sort(array):
    obj = QuickSort()
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    sorted_array = sorted(array)
    assert obj.sort(array) == sorted_array
