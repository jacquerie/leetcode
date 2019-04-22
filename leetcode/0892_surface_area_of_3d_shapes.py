# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):

    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def surfaceArea(self, grid):
        result = 0

        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                result += self.singleSurfaceArea(grid, i, j)

        return result

    def singleSurfaceArea(self, grid, i, j):
        result = 2 if grid[i][j] else 0

        for neighbor in self.getNeighbors(grid, i, j):
            if grid[i][j] > neighbor:
                result += grid[i][j] - neighbor

        return result

    def getNeighbors(self, grid, i, j):
        result = []

        for h, k in self.DIRECTIONS:
            result.append(self.getNeighbor(grid, i + h, j + k))

        return result

    def getNeighbor(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        return grid[i][j]


if __name__ == '__main__':
    solution = Solution()

    assert 10 == solution.surfaceArea([[2]])
    assert 34 == solution.surfaceArea([
        [1, 2],
        [3, 4],
    ])
    assert 16 == solution.surfaceArea([
        [1, 0],
        [0, 2],
    ])
    assert 32 == solution.surfaceArea([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ])
    assert 46 == solution.surfaceArea([
        [2, 2, 2],
        [2, 1, 2],
        [2, 2, 2],
    ])
