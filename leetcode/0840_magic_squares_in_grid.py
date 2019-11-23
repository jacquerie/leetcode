# -*- coding: utf-8 -*-


class Solution(object):
    def isMagicSquareCenteredHere(self, grid, i, j):
        all_nine_numbers = sorted([
            grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],
            grid[i][j - 1], grid[i][j], grid[i][j + 1],
            grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1],
        ]) == list(range(1, 10))

        all_sums_equal = len(set([
            # rows
            grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1],
            grid[i][j - 1] + grid[i][j] + grid[i][j + 1],
            grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1],
            # cols
            grid[i - 1][j - 1] + grid[i][j - 1] + grid[i + 1][j - 1],
            grid[i - 1][j] + grid[i][j] + grid[i + 1][j],
            grid[i - 1][j + 1] + grid[i][j + 1] + grid[i + 1][j + 1],
            # diags
            grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1],
            grid[i + 1][j - 1] + grid[i][j] + grid[i - 1][j + 1],
        ])) == 1

        return all_nine_numbers and all_sums_equal

    def numMagicSquaresInside(self, grid):
        result = 0
        num_rows, num_cols = len(grid), len(grid[0])

        for i in range(1, num_rows - 1):
            for j in range(1, num_cols - 1):
                if self.isMagicSquareCenteredHere(grid, i, j):
                    result += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.numMagicSquaresInside([
        [4, 3, 8, 4],
        [9, 5, 1, 9],
        [2, 7, 6, 2],
    ])
    assert 0 == solution.numMagicSquaresInside([
        [10, 3, 5],
        [1, 6, 11],
        [7, 9, 2],
    ])
