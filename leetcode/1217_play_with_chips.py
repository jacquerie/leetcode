# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def minCostToMoveChips(self, chips):
        count_even, count_odd = 0, 0
        for chip in chips:
            if chip % 2 == 0:
                count_even += 1
            else:
                count_odd += 1

        return min(count_even, count_odd)


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.minCostToMoveChips([1, 2, 3])
    assert 2 == solution.minCostToMoveChips([2, 2, 2, 3, 3])
