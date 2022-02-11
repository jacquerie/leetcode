# -*- coding: utf-8 -*-

import heapq


class Solution:
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, key=lambda xy: xy[0] * xy[0] + xy[1] * xy[1])


if __name__ == "__main__":
    solution = Solution()

    assert [[-2, 2]] == solution.kClosest([[1, 3], [-2, 2]], 1)
    assert [[3, 3], [-2, 4]] == solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
