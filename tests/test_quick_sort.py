# coding=utf-8

from algorithms.quick_sort import QuickSort, QuickSortInPlace


def test_quick_sort(arrays):
    obj = QuickSort()
    for array in arrays:
        sorted_array = sorted(array)
        assert obj.sort(array) == sorted_array


def test_quick_sort_in_place(arrays):
    obj = QuickSortInPlace()
    for array in arrays:
        obj.sort(array)
        assert array == sorted(array)
