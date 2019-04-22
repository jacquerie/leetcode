# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def findPeakElement(self, nums):
        first, last = 0, len(nums) - 1

        while first < last:
            mid = (first + last) // 2
            if nums[mid] > nums[mid + 1]:
                last = mid
            else:
                first = mid + 1

        return first


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.findPeakElement([1, 2, 3, 1])
    assert 5 == solution.findPeakElement([1, 2, 1, 3, 5, 6, 4])
