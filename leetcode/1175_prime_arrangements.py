# -*- coding: utf-8 -*-

from math import factorial


class Solution:
    PRIMES = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]

    def numPrimeArrangements(self, n: int) -> int:
        p = len([_ for _ in self.PRIMES if _ <= n])
        return (factorial(p) * factorial(n - p)) % (10**9 + 7)


if __name__ == "__main__":
    solution = Solution()

    assert 12 == solution.numPrimeArrangements(5)
    assert 682289015 == solution.numPrimeArrangements(100)
