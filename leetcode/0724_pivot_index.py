# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, total_sum = 0, sum(nums)
        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num

        return -1


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.pivotIndex([1, 7, 3, 6, 5, 6])
    assert -1 == solution.pivotIndex([1, 2, 3])
