# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def projectionArea(self, grid):
        result = 0

        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]:
                    result += 1

        for i in xrange(len(grid)):
            partial = 0
            for j in xrange(len(grid[0])):
                partial = max(partial, grid[i][j])
            result += partial

        for j in xrange(len(grid[0])):
            partial = 0
            for i in xrange(len(grid)):
                partial = max(partial, grid[i][j])
            result += partial

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 5 == solution.projectionArea([[2]])
    assert 17 == solution.projectionArea([[1, 2], [3, 4]])
    assert 8 == solution.projectionArea([[1, 0], [0, 2]])
    assert 14 == solution.projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    assert 21 == solution.projectionArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]])
