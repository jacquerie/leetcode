# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for row in matrix:
            if len(row) != len(set(row)):
                return False

        for col in zip(*matrix):
            if len(col) != len(set(col)):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    assert solution.checkValid([[1, 2, 3], [3, 1, 2], [2, 3, 1]])
    assert not solution.checkValid([[1, 1, 1], [1, 2, 3], [1, 2, 3]])
