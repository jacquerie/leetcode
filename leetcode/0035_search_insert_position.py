# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def searchInsert(self, nums, target):
        for i, el in enumerate(nums):
            if el >= target:
                return i
        return i + 1


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.searchInsert([1, 3, 5, 6], 5)
    assert 1 == solution.searchInsert([1, 3, 5, 6], 2)
    assert 4 == solution.searchInsert([1, 3, 5, 6], 7)
    assert 0 == solution.searchInsert([1, 3, 5, 6], 0)
