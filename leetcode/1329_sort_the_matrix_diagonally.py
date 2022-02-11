# -*- coding: utf-8 -*-

from collections import defaultdict
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diags = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diags[i - j].append(mat[i][j])

        for diag in diags.values():
            diag.sort(reverse=True)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = diags[i - j].pop()

        return mat


if __name__ == "__main__":
    solution = Solution()

    assert [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3],] == solution.diagonalSort(
        [
            [3, 3, 1, 1],
            [2, 2, 1, 2],
            [1, 1, 1, 2],
        ]
    )
