# -*- coding: utf-8 -*-

import functools
import operator


class Solution:
    def choose(self, n, k):
        k = min(k, n - k)
        numerator = functools.reduce(operator.mul, range(n, n - k, -1), 1)
        denominator = functools.reduce(operator.mul, range(1, k + 1), 1)

        return numerator // denominator

    def uniquePaths(self, m, n):
        return self.choose(m + n - 2, m - 1)


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.uniquePaths(3, 2)
    assert 28 == solution.uniquePaths(7, 3)
    assert 1 == solution.uniquePaths(2, 1)
    assert 6435 == solution.uniquePaths(9, 8)
