# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def maxProfit(self, prices):
        result = 0

        for i, price in enumerate(prices[:-1]):
            result += max(0, prices[i + 1] - price)

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 7 == solution.maxProfit([7, 1, 5, 3, 6, 4])
    assert 4 == solution.maxProfit([1, 2, 3, 4, 5])
    assert 0 == solution.maxProfit([7, 6, 4, 3, 1])
