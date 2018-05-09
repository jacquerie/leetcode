# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def countPrimes(self, n):
        if n == 0 or n == 1:
            return 0

        result = [1] * n
        result[0] = result[1] = 0

        for i, el in enumerate(result):
            if el:
                for j in xrange(i * i, n, i):
                    result[j] = 0

        return sum(result)


if __name__ == '__main__':
    solution = Solution()

    assert 0 == solution.countPrimes(0)
    assert 0 == solution.countPrimes(1)
    assert 0 == solution.countPrimes(2)
    assert 1 == solution.countPrimes(3)
    assert 2 == solution.countPrimes(4)
    assert 2 == solution.countPrimes(5)
    assert 3 == solution.countPrimes(6)
    assert 3 == solution.countPrimes(7)
    assert 4 == solution.countPrimes(8)
    assert 4 == solution.countPrimes(9)
    assert 4 == solution.countPrimes(10)
    assert 4 == solution.countPrimes(11)
    assert 5 == solution.countPrimes(12)
