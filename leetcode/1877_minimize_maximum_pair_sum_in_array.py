# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        i, result = 0, float("-inf")
        while i <= len(nums) // 2:
            i, result = i + 1, max(result, nums[i] + nums[-i - 1])
        return result


if __name__ == "__main__":
    solution = Solution()

    assert 7 == solution.minPairSum([3, 5, 2, 3])
    assert 8 == solution.minPairSum([3, 5, 4, 2, 4, 6])
