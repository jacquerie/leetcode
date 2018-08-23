# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def __eq__(self, other):
        return (
            other is not None and
            self.val == other.val and
            self.isLeaf == other.isLeaf and
            self.topLeft == other.topLeft and
            self.topRight == other.topRight and
            self.bottomLeft == other.bottomLeft and
            self.bottomRight == other.bottomRight
        )


class Solution(object):
    def construct(self, grid):
        return self.constructSubgrid(grid, 0, len(grid), 0, len(grid[0]))

    def constructSubgrid(self, grid, min_row, max_row, min_col, max_col):
        allEqual = self.allEqual(grid, min_row, max_row, min_col, max_col)
        if allEqual is not None:
            return Node(allEqual, True, None, None, None, None)

        topLeft = self.constructSubgrid(
            grid, min_row, (min_row + max_row) // 2, min_col, (min_col + max_col) // 2)
        topRight = self.constructSubgrid(
            grid, min_row, (min_row + max_row) // 2, (min_col + max_col) // 2, max_col)
        bottomLeft = self.constructSubgrid(
            grid, (min_row + max_row) // 2, max_row, min_col, (min_col + max_col) // 2)
        bottomRight = self.constructSubgrid(
            grid, (min_row + max_row) // 2, max_row, (min_col + max_col) // 2, max_col)

        return Node(None, False, topLeft, topRight, bottomLeft, bottomRight)

    def allEqual(self, grid, min_row, max_row, min_col, max_col):
        for i in xrange(min_row, max_row):
            for j in xrange(min_col, max_col):
                if grid[i][j] != grid[min_row][min_col]:
                    return None
        return 1 == grid[min_row][min_col]


if __name__ == '__main__':
    solution = Solution()

    t0_8 = Node(True, True, None, None, None, None)
    t0_7 = Node(True, True, None, None, None, None)
    t0_6 = Node(False, True, None, None, None, None)
    t0_5 = Node(False, True, None, None, None, None)
    t0_4 = Node(False, True, None, None, None, None)
    t0_3 = Node(True, True, None, None, None, None)
    t0_2 = Node(None, False, t0_5, t0_6, t0_7, t0_8)
    t0_1 = Node(True, True, None, None, None, None)
    t0_0 = Node(None, False, t0_1, t0_2, t0_3, t0_4)

    assert t0_0 == solution.construct([
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
    ])
