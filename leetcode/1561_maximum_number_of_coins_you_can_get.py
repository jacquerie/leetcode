# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(
            pile
            for i, pile in enumerate(sorted(piles, reverse=True))
            if i % 2 == 1 and i <= 2 * len(piles) / 3
        )


if __name__ == "__main__":
    solution = Solution()

    assert 9 == solution.maxCoins([2, 4, 1, 2, 7, 8])
    assert 4 == solution.maxCoins([2, 4, 5])
    assert 18 == solution.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4])
