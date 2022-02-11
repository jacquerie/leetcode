# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {el: i for i, el in enumerate(sorted(set(arr)), 1)}
        return [ranks[el] for el in arr]


if __name__ == "__main__":
    solution = Solution()

    assert [4, 1, 2, 3] == solution.arrayRankTransform([40, 10, 20, 30])
    assert [1, 1, 1] == solution.arrayRankTransform([100, 100, 100])
    assert [5, 3, 4, 2, 8, 6, 7, 1, 3] == solution.arrayRankTransform(
        [37, 12, 28, 9, 100, 56, 80, 5, 12]
    )
