# coding=utf-8

from algorithms.breadth_first_search import FindPathExist


def test_find_path_exist(directed_graph):
    obj = FindPathExist()
    assert obj.search(directed_graph, 'A', 'A')
    assert obj.search(directed_graph, 'A', 'F')
    assert not obj.search(directed_graph, 'A', 'H')
    assert not obj.search(directed_graph, 'A', 'I')
    assert not obj.search(directed_graph, 'B', 'C')
