# -*- coding: utf-8 -*-


class Solution:
    def minPathSum(self, grid):
        result = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

        result[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            result[i][0] = grid[i][0] + result[i - 1][0]
        for j in range(1, len(grid[0])):
            result[0][j] = grid[0][j] + result[0][j - 1]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                result[i][j] = grid[i][j] + min(result[i - 1][j], result[i][j - 1])

        return result[-1][-1]


if __name__ == '__main__':
    solution = Solution()

    assert 7 == solution.minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1],
    ])
