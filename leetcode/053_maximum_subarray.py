# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def maxSubArray(self, nums):
        max_ending_here = max_so_far = nums[0]

        for num in nums[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far


if __name__ == '__main__':
    solution = Solution()

    assert 6 == solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
