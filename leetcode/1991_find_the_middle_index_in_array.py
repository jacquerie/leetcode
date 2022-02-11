# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        current_sum, total_sum = 0, sum(nums)
        for i, num in enumerate(nums):
            if current_sum * 2 + num == total_sum:
                return i
            current_sum += num
        return -1


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.findMiddleIndex([2, 3, -1, 8, 4])
    assert 2 == solution.findMiddleIndex([1, -1, 4])
    assert -1 == solution.findMiddleIndex([2, 5])
    assert 0 == solution.findMiddleIndex([1])
