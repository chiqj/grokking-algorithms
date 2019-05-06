# coding=utf-8

from algorithms.merge_sort import MergeSort


def test_merge_sort(arrays):
    obj = MergeSort()
    for array in arrays:
        sorted_array = sorted(array)
        assert obj.sort(array) == sorted_array
