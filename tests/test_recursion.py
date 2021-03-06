# coding=utf-8

import pytest

from algorithms.recursion import Factorial, Fibonacci, EuclideanAlgorithm


def test_factorial():
    obj = Factorial()
    assert obj.run(0) == 1
    assert obj.run(1) == 1
    assert obj.run(5) == 120
    with pytest.raises(ValueError):
        obj.run(-1)


def test_fibonacci():
    obj = Fibonacci()
    assert obj.run(0) == 0
    assert obj.run(1) == 1
    assert obj.run(2) == 1
    assert obj.run(10) == 55
    with pytest.raises(ValueError):
        obj.run(-1)


def test_euclidean_algorithm():
    obj = EuclideanAlgorithm()
    assert obj.gcd(5, 5) == 5
    assert obj.gcd(2, 10) == 2
    assert obj.gcd(3, 7) == 1
    assert obj.gcd(50, 20) == 10
