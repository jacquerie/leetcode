# -*- coding: utf-8 -*-

from collections import deque


class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    result += 1
                    self.deleteIsland(grid, i, j)

        return result

    def deleteIsland(self, grid, i, j):
        stack = deque([(i, j)])
        while stack:
            x, y = stack.pop()
            grid[x][y] = '0'
            if 0 < x and grid[x - 1][y] == '1':
                stack.append((x - 1, y))
            if 0 < y and grid[x][y - 1] == '1':
                stack.append((x, y - 1))
            if x < len(grid) - 1 and grid[x + 1][y] == '1':
                stack.append((x + 1, y))
            if y < len(grid[0]) - 1 and grid[x][y + 1] == '1':
                stack.append((x, y + 1))


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.numIslands([
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ])
    assert 3 == solution.numIslands([
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ])
