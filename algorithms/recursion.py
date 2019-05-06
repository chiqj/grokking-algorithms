# coding=utf-8


class Factorial:
    def run(self, x: int) -> int:
        if x < 0:
            raise ValueError('invalid x, should be a nonnegative number.')
        elif x == 0:
            return 1
        else:
            return x * self.run(x-1)


class Fibonacci:
    def run(self, x: int) -> int:
        if x < 0:
            raise ValueError('invalid x, should be a nonnegative number.')
        elif x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return self.run(x-2) + self.run(x-1)


class EuclideanAlgorithm:
    def gcd(self, a: int, b: int) -> int:
        """ Calculate greatest common divisor（最大公约数）."""
        if a < b:
            a, b = b, a
        if a % b == 0:
            return b
        else:
            return self.gcd(a % b, b)
