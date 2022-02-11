# -*- coding: utf-8 -*-


class Solution:
    def setZeroes(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for h in range(len(matrix)):
                        if matrix[h][j] == 0:
                            continue
                        matrix[h][j] = None
                    for k in range(len(matrix[0])):
                        if matrix[i][k] == 0:
                            continue
                        matrix[i][k] = None

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] is None:
                    matrix[i][j] = 0


if __name__ == "__main__":
    solution = Solution()

    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]

    assert solution.setZeroes(matrix) is None
    assert [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ] == matrix

    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5],
    ]

    assert solution.setZeroes(matrix) is None
    assert [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0],
    ] == matrix
