# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        nums.sort(reverse=True)

        current_sum = 0
        for i, num in enumerate(nums):
            current_sum += num
            if 2 * current_sum > total_sum:
                return nums[: i + 1]


if __name__ == "__main__":
    solution = Solution()

    assert [10, 9] == solution.minSubsequence([4, 3, 10, 9, 8])
    assert [7, 7, 6] == solution.minSubsequence([4, 4, 7, 6, 7])
    assert [6] == solution.minSubsequence([6])
