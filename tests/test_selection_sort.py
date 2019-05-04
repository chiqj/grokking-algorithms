# coding=utf-8


from algorithms.selection_sort import SelectionSort


def test_find_min_element():
    obj = SelectionSort()
    array = [2, 3, 1, 4, 5]
    assert obj.find_min_element(array) == 2


def test_selection_sort():
    obj = SelectionSort()
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    sorted_array = sorted(array)
    assert obj.sort(array) == sorted_array
