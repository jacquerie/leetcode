# -*- coding: utf-8 -*-


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i - 1][j - 1] != matrix[i][j]:
                    return False

        return True


if __name__ == '__main__':
    solution = Solution()

    assert solution.isToeplitzMatrix([
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2],
    ])
    assert not solution.isToeplitzMatrix([
        [1, 2],
        [2, 2],
    ])
