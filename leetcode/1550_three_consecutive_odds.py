# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds_count = 0
        for el in arr:
            if el % 2 == 0:
                odds_count = 0
            else:
                odds_count += 1
            if odds_count == 3:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()

    assert not solution.threeConsecutiveOdds([2, 6, 4, 1])
    assert solution.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12])
