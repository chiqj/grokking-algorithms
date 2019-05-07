# coding=utf-8

import pytest


@pytest.fixture
def arrays():
    return (
        [6, 4, 4, 1, 6, 7, 10, 4, 1, 2, 5, 10, 3, 3, 4, 2, 4, 1, 10, 8],
        [6, 4, 4, 1, 6, 7, 10, 4, 1, 2, 5, 10, 3, 3, 4, 2, 4, 1, 10, 8],
        [6, 7, 9, 7, 5, 8, 7, 2, 9, 6, 10, 9, 8, 2, 9, 8, 2, 6, 2, 7],
        [],
        [1],
        [2, 1],
        [1, 2, 3, 4],
        [5, 5, 5, 5, 5],
    )


@pytest.fixture
def directed_graph():
    graph = {
        'A': ['B', 'C', 'E'],
        'B': ['D'],
        'C': ['D'],
        'D': [],
        'E': ['F', 'G'],
        'F': [],
        'G': [],
        'H': ['B'],
    }
    return graph


@pytest.fixture
def weighted_graphs():
    yield {
        'start': {
            'a': 6,
            'b': 2,
        },
        'a': {
            'end': 1,
        },
        'b': {
            'a': 3,
            'end': 5,
        },
        'end': {},
    }
    yield {
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
    yield {
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
    yield {
        'start': {
            'a': 2,
            'b': 2,
        },
        'a': {
            'b': 2,
        },
        'b': {
            'c': 2,
            'end': 2,
        },
        'c': {
            'a': -1,
            'end': 2,
        },
        'end': {},
    }
