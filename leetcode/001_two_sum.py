# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def twoSum(self, nums, target):
        numsMap = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if target - num in numsMap and numsMap[target - num] != i:
                return [i, numsMap[target - num]]


if __name__ == '__main__':
    solution = Solution()

    assert [0, 1] == solution.twoSum([2, 7, 11, 15], 9)
