# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        top_bottom_skyline = [max(row) for row in zip(*grid)]
        left_right_skyline = [max(row) for row in grid]

        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_height = min(left_right_skyline[i], top_bottom_skyline[j])
                result += max_height - grid[i][j]

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 35 == solution.maxIncreaseKeepingSkyline([
        [3, 0, 8, 4],
        [2, 4, 5, 7],
        [9, 2, 6, 3],
        [0, 3, 1, 0],
    ])
