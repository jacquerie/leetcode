# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_num, max_num = min(nums), max(nums)
        return sum(min_num < num < max_num for num in nums)


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.countElements([11, 7, 2, 15])
    assert 2 == solution.countElements([-3, 3, 3, 90])
