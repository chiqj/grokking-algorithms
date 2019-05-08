# coding=utf-8

import pytest

from algorithms.dijkstra_algorithm import DijkstraAlgorithm

graph1 = {
    'start': {
        'a': 5,
        'b': 2,
    },
    'a': {
        'c': 4,
        'd': 2,
    },
    'b': {
        'a': 8,
        'd': 7,
    },
    'c': {
        'd': 6,
        'end': 3,
    },
    'd': {
        'end': 1,
    },
    'end': {},
}

graph2 = {
    'start': {
        'a': 10,
    },
    'a': {
        'c': 20,
    },
    'b': {
        'a': 1,
    },
    'c': {
        'b': 1,
        'end': 30,
    },
    'end': {},
}


@pytest.mark.parametrize(
    ('costs', 'processed', 'result'),
    (
        ({}, set(), None),
        ({'a': 1, 'b': 2, 'c': 3}, {'a'}, 'b'),
        ({'a': 1, 'b': float('inf')}, {}, 'a'),
        ({'a': 1, 'b': 2, 'c': 3}, {'a', 'b', 'c'}, None),
    ),
)
def test_find_min_cost_vertice(costs, processed, result):
    obj = DijkstraAlgorithm()
    if result is None:
        assert obj.find_min_cost_vertice(costs, processed) is result
    else:
        assert obj.find_min_cost_vertice(costs, processed) == result


@pytest.mark.parametrize(
    ('parents', 'result'),
    (
        ({'end': 'b', 'b': 'a', 'a': 'start'}, ['start', 'a', 'b', 'end']),
        ({'end': 'start'}, ['start', 'end']),
    ),
)
def test_get_path(parents, result):
    obj = DijkstraAlgorithm()
    assert obj.get_path(parents, 'start', 'end') == result


@pytest.mark.parametrize(
    ('graph', 'cost', 'path'),
    (
        (graph1, 8, ['start', 'a', 'd', 'end']),
        (graph2, 60, ['start', 'a', 'c', 'end']),
    )
)
def test_dijkstra_algorithm(graph, cost, path):
    obj = DijkstraAlgorithm()
    assert obj.run(graph, 'start', 'end') == (cost, path)
