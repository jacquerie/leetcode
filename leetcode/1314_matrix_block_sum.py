# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        sums = [[0 for j in range(len(mat[0]) + 1)] for i in range(len(mat) + 1)]
        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                sums[i][j] = (
                    mat[i - 1][j - 1]
                    + sums[i - 1][j]
                    + sums[i][j - 1]
                    - sums[i - 1][j - 1]
                )

        result = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                x1, x2 = max(0, i - K), min(len(mat), i + K + 1)
                y1, y2 = max(0, j - K), min(len(mat[0]), j + K + 1)
                result[i][j] = sums[x2][y2] - sums[x2][y1] - sums[x1][y2] + sums[x1][y1]

        return result


if __name__ == "__main__":
    solution = Solution()

    assert [[12, 21, 16], [27, 45, 33], [24, 39, 28],] == solution.matrixBlockSum(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
        1,
    )
    assert [[45, 45, 45], [45, 45, 45], [45, 45, 45],] == solution.matrixBlockSum(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
        2,
    )
