# -*- coding: utf-8 -*-

from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    result += 1 if self.exploreIsland(grid, i, j) else 0

        return result

    def exploreIsland(self, grid: List[List[int]], i: int, j: int) -> bool:
        result = True

        stack = deque([(i, j)])
        while stack:
            x, y = stack.pop()
            grid[x][y] = 1
            if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
                result = False
            if 0 < x and grid[x - 1][y] == 0:
                stack.append((x - 1, y))
            if 0 < y and grid[x][y - 1] == 0:
                stack.append((x, y - 1))
            if x < len(grid) - 1 and grid[x + 1][y] == 0:
                stack.append((x + 1, y))
            if y < len(grid[0]) - 1 and grid[x][y + 1] == 0:
                stack.append((x, y + 1))

        return result


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.closedIsland(
        [
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0],
        ]
    )
    assert 1 == solution.closedIsland(
        [
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
        ]
    )
    assert 2 == solution.closedIsland(
        [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ]
    )
