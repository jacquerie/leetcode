# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True

        for _ in range(3):
            self.rotate(mat)
            if mat == target:
                return True

        return False

    def rotate(self, mat: List[List[int]]):
        n = len(mat)

        for i in range(n):
            for j in range(i + 1):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        for i in range(n):
            for j in range(n // 2):
                mat[i][j], mat[i][n - j - 1] = mat[i][n - j - 1], mat[i][j]


if __name__ == '__main__':
    solution = Solution()

    assert solution.findRotation([
        [0, 1],
        [1, 0],
    ], [
        [1, 0],
        [0, 1],
    ])
    assert not solution.findRotation([
        [0, 1],
        [1, 1],
    ], [
        [1, 0],
        [0, 1],
    ])
    assert solution.findRotation([
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ], [
        [1, 1, 1],
        [0, 1, 0],
        [0, 0, 0],
    ])
