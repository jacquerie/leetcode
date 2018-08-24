# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def totalHammingDistance(self, nums):
        result = 0

        for digit in xrange(32):
            partial = 0
            for num in nums:
                partial += (num >> digit) & 1
            result += partial * (len(nums) - partial)

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 6 == solution.totalHammingDistance([4, 14, 2])
