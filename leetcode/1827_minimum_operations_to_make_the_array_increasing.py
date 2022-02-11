# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        current_num, result = 0, 0
        for num in nums:
            if num <= current_num:
                current_num += 1
                result += current_num - num
            else:
                current_num = num
        return result


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.minOperations([1, 1, 1])
    assert 14 == solution.minOperations([1, 5, 2, 4, 1])
    assert 0 == solution.minOperations([8])
