# -*- coding: utf-8 -*-

from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid):
        result = 0
        if not grid:
            return result

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    result = max(result, self.measureAndDeleteIsland(grid, i, j))

        return result

    def measureAndDeleteIsland(self, grid, i, j):
        result = set()

        queue = deque([(i, j)])
        while queue:
            x, y = queue.pop()
            grid[x][y] = 0
            if 0 < x and grid[x - 1][y]:
                queue.append((x - 1, y))
            if 0 < y and grid[x][y - 1]:
                queue.append((x, y - 1))
            if x < len(grid) - 1 and grid[x + 1][y]:
                queue.append((x + 1, y))
            if y < len(grid[0]) - 1 and grid[x][y + 1]:
                queue.append((x, y + 1))
            result.add((x, y))

        return len(result)


if __name__ == "__main__":
    solution = Solution()

    assert 6 == solution.maxAreaOfIsland(
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
    assert 0 == solution.maxAreaOfIsland(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    assert 4 == solution.maxAreaOfIsland(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
        ]
    )
