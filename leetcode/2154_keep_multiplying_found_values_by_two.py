# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = set(nums)
        while original in nums_set:
            original *= 2
        return original


if __name__ == "__main__":
    solution = Solution()

    assert 24 == solution.findFinalValue([5, 3, 6, 1, 12], 3)
    assert 4 == solution.findFinalValue([2, 7, 9], 4)
