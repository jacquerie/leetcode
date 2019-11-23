# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        elements = [grid[i][j] for i in xrange(m) for j in xrange(n)]
        shifted = elements[-(k % (m * n)):] + elements[:-(k % (m * n))]
        return [[shifted[i * n + j] for j in xrange(n)] for i in xrange(m)]


if __name__ == '__main__':
    solution = Solution()

    assert [
        [9, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ] == solution.shiftGrid([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ], 1)
    assert [
        [12, 0, 21, 13],
        [3, 8, 1, 9],
        [19, 7, 2, 5],
        [4, 6, 11, 10],
    ] == solution.shiftGrid([
        [3, 8, 1, 9],
        [19, 7, 2, 5],
        [4, 6, 11, 10],
        [12, 0, 21, 13],
    ], 4)
    assert [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ] == solution.shiftGrid([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ], 9)
    assert [
        [6], [5], [1], [2], [3], [4], [7],
    ] == solution.shiftGrid([
        [1], [2], [3], [4], [7], [6], [5],
    ], 23)
