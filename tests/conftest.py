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
