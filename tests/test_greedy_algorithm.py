# coding=utf-8

from algorithms.greedy_algorithm import GreedyAlgorithm


def test_greedy_algorithm():
    stations = {
        'kone': {'id', 'nv', 'ut'},
        'ktwo': {'wa', 'id', 'mt'},
        'kthree': {'or', 'nv', 'ca'},
        'kfour': {'nv', 'ut'},
        'kfive': {'ca', 'az'},
    }
    states = {'mt', 'wa', 'or', 'ca', 'ut', 'id', 'az', 'nv'}
    result = (
        {'ktwo', 'kthree', 'kfour', 'kfive'},
        {'kone', 'ktwo', 'kthree', 'kfive'},
    )
    obj = GreedyAlgorithm()
    assert obj.run(stations, states) in result
