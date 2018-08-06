# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def search(self, nums, target):
        first, last = 0, len(nums) - 1

        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == target:
                return mid
            elif ((nums[first] <= nums[mid] and nums[first] <= target < nums[mid]) or
                  (nums[first] > nums[mid] and not (nums[mid] < target <= nums[last]))):
                last = mid - 1
            else:
                first = mid + 1

        return -1


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.search([4, 5, 6, 7, 0, 1, 2], 0)
    assert -1 == solution.search([4, 5, 6, 7, 0, 1, 2], 3)
