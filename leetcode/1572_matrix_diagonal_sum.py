# -*- coding: utf-8 -*-


from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n, result = len(mat), 0
        for i in range(n):
            result += mat[i][i] + mat[n - i - 1][i]
        return result - (mat[n // 2][n // 2] if n % 2 == 1 else 0)


if __name__ == "__main__":
    solution = Solution()

    assert 25 == solution.diagonalSum(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )
    assert 8 == solution.diagonalSum(
        [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
    )
    assert 5 == solution.diagonalSum([[5]])
