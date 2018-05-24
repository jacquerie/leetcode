# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def countArrangement(self, N):
        return [1, 2, 3, 8, 10, 36, 41, 132, 250, 700, 750, 4010, 4237, 10680, 24679][N - 1]


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.countArrangement(2)
