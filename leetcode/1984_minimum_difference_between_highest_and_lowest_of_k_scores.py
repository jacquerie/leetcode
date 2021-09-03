# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        result = float('inf')
        for i in range(len(nums) - k + 1):
            result = min(result, nums[i + k - 1] - nums[i])
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 0 == solution.minimumDifference([90], 1)
    assert 2 == solution.minimumDifference([9, 4, 1, 7], 2)
