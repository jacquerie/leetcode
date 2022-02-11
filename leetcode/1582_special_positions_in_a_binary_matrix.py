# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and self.isSpecial(mat, i, j):
                    result += 1
        return result

    def isSpecial(self, mat: List[List[int]], i: int, j: int) -> bool:
        for k in range(len(mat)):
            if i != k and mat[k][j] == 1:
                return False
        for k in range(len(mat[0])):
            if j != k and mat[i][k] == 1:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()

    assert 1 == solution.numSpecial(
        [
            [1, 0, 0],
            [0, 0, 1],
            [1, 0, 0],
        ]
    )
    assert 3 == solution.numSpecial(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
    )
    assert 2 == solution.numSpecial(
        [
            [0, 0, 0, 1],
            [1, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ]
    )
    assert 3 == solution.numSpecial(
        [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1],
        ]
    )
