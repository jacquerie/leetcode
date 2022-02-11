# -*- coding: utf-8 -*-


class Solution:
    def islandPerimeter(self, grid):
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if i == 0 or grid[i - 1][j] == 0:
                        result += 1
                    if i == len(grid) - 1 or grid[i + 1][j] == 0:
                        result += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        result += 1
                    if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                        result += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert 16 == solution.islandPerimeter(
        [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0],
        ]
    )
