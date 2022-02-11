# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [candy + extraCandies >= max(candies) for candy in candies]


if __name__ == "__main__":
    solution = Solution()

    assert [True, True, True, False, True] == solution.kidsWithCandies(
        [2, 3, 5, 1, 3], 3
    )
    assert [True, False, False, False, False] == solution.kidsWithCandies(
        [4, 2, 1, 1, 2], 1
    )
    assert [True, False, True] == solution.kidsWithCandies([12, 1, 12], 10)
