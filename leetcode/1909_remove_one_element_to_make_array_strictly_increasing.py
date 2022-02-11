# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        previous, violation_seen = float("-inf"), False
        for i, num in enumerate(nums):
            if previous < num:
                previous = num
            else:
                if violation_seen:
                    return False
                previous, violation_seen = (
                    num if i == 1 or nums[i - 2] < num else previous,
                    True,
                )
        return True


if __name__ == "__main__":
    solution = Solution()

    assert solution.canBeIncreasing([1, 2, 10, 5, 7])
    assert not solution.canBeIncreasing([2, 3, 1, 2])
    assert not solution.canBeIncreasing([1, 1, 1])
    assert solution.canBeIncreasing([1, 2, 3])
