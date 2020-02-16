# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i, j, result = 0, len(grid[0]) - 1, 0
        while i < len(grid) and j >= 0:
            if grid[i][j] < 0:
                j -= 1
                result += len(grid) - i
            else:
                i += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 8 == solution.countNegatives([
        [4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3],
    ])
    assert 0 == solution.countNegatives([
        [3, 2],
        [1, 0],
    ])
    assert 3 == solution.countNegatives([
        [1, -1],
        [-1, -1],
    ])
    assert 1 == solution.countNegatives([
        [-1],
    ])
