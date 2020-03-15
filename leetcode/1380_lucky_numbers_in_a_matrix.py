# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_rows = {min(row) for row in matrix}
        max_cols = {max(col) for col in zip(*matrix)}
        return [el for el in min_rows & max_cols]


if __name__ == '__main__':
    solution = Solution()

    assert [15] == solution.luckyNumbers([
        [3, 7, 8],
        [9, 11, 13],
        [15, 16, 17],
    ])
    assert [12] == solution.luckyNumbers([
        [1, 10, 4, 2],
        [9, 3, 8, 7],
        [15, 16, 17, 12],
    ])
    assert [7] == solution.luckyNumbers([
        [7, 8],
        [1, 2],
    ])
