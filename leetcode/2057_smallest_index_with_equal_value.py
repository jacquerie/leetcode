# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i % 10 == num:
                return i
        return -1


if __name__ == "__main__":
    solution = Solution()

    assert 0 == solution.smallestEqual([0, 1, 2])
    assert 2 == solution.smallestEqual([4, 3, 2, 1])
    assert -1 == solution.smallestEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    assert 1 == solution.smallestEqual([2, 1, 3, 5, 2])
