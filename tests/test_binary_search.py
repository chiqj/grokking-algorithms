# coding=utf-8

from algorithms.binary_search import BinarySearch


def test_binary_search():
    obj = BinarySearch()
    test_list = [2, 4, 6, 8, 10]
    assert obj.search(test_list, 2) == 0
    assert obj.search(test_list, 4) == 1
    assert obj.search(test_list, 10) == 4
    assert obj.search(test_list, 3) is None
    assert obj.search(test_list, 1) is None
    assert obj.search(test_list, 11) is None
