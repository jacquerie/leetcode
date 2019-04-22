# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        result = [1] * len(nums)

        for i in xrange(len(nums)):
            partial = result[i]
            for j in xrange(i):
                if nums[i] > nums[j]:
                    partial = max(partial, 1 + result[j])
            result[i] = partial

        return max(result)


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
