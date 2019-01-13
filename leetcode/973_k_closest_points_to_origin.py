# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import heapq


class Solution(object):
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, key=lambda (x, y): x * x + y * y)


if __name__ == '__main__':
    solution = Solution()

    assert [[-2, 2]] == solution.kClosest([[1, 3], [-2, 2]], 1)
    assert [[3, 3], [-2, 4]] == solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
