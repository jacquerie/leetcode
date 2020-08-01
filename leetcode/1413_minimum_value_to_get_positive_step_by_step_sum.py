# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        current_sum, result = 0, 0
        for num in nums:
            current_sum += num
            result = max(result, -current_sum)
        return result + 1


if __name__ == '__main__':
    solution = Solution()

    assert 5 == solution.minStartValue([-3, 2, -3, 4, 2])
    assert 1 == solution.minStartValue([1, 2])
    assert 5 == solution.minStartValue([1, -2, -3])
