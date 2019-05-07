# coding=utf-8

from algorithms.breadth_first_search import FindPathExist


def test_find_path_exist(graph):
    obj = FindPathExist()
    assert obj.search(graph, 'A', 'A')
    assert obj.search(graph, 'A', 'F')
    assert not obj.search(graph, 'A', 'H')
    assert not obj.search(graph, 'A', 'I')
    assert not obj.search(graph, 'B', 'C')
