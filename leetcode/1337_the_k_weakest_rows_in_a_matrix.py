# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for _, i in sorted((sum(row), i) for i, row in enumerate(mat))[:k]]


if __name__ == "__main__":
    solution = Solution()

    assert [2, 0, 3] == solution.kWeakestRows(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ],
        3,
    )
    assert [0, 2] == solution.kWeakestRows(
        [
            [1, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
        ],
        2,
    )
