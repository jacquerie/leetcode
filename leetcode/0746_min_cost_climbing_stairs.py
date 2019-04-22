# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def minCostClimbingStairs(self, cost):
        previous, current = cost[0], cost[1]
        for i in xrange(2, len(cost)):
            previous, current = current, cost[i] + min(previous, current)
        return min(previous, current)


if __name__ == '__main__':
    solution = Solution()

    assert 15 == solution.minCostClimbingStairs([10, 15, 20])
    assert 6 == solution.minCostClimbingStairs([
        1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
