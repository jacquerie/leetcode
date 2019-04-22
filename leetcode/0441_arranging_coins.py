# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def arrangeCoins(self, n):
        i, total = 0, 0

        while total <= n:
            i += 1
            total += i

        return i - 1


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.arrangeCoins(5)
    assert 3 == solution.arrangeCoins(8)
    assert 0 == solution.arrangeCoins(0)
    assert 1 == solution.arrangeCoins(1)
