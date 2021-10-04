# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        result = [[None for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = original[i * n + j]
        return result


if __name__ == '__main__':
    solution = Solution()

    assert [[1, 2], [3, 4]] == solution.construct2DArray([1, 2, 3, 4], 2, 2)
    assert [[1, 2, 3]] == solution.construct2DArray([1, 2, 3], 1, 3)
    assert [] == solution.construct2DArray([1, 2], 1, 1)
    assert [] == solution.construct2DArray([3], 1, 2)
