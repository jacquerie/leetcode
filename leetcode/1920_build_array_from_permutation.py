# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


if __name__ == '__main__':
    solution = Solution()

    assert [0, 1, 2, 4, 5, 3] == solution.buildArray([0, 2, 1, 5, 3, 4])
    assert [4, 5, 0, 1, 2, 3] == solution.buildArray([5, 0, 1, 2, 3, 4])
