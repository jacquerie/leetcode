# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current_sum, result, current_value = 0, float("-inf"), float("-inf")
        for num in nums:
            current_sum = current_sum + num if num > current_value else num
            result = max(current_sum, result)
            current_value = num
        return result


if __name__ == "__main__":
    solution = Solution()

    assert 65 == solution.maxAscendingSum([10, 20, 30, 5, 10, 50])
    assert 150 == solution.maxAscendingSum([10, 20, 30, 40, 50])
    assert 33 == solution.maxAscendingSum([12, 17, 15, 13, 10, 11, 12])
    assert 100 == solution.maxAscendingSum([100, 10, 1])
