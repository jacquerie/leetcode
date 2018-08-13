# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def singleNumber(self, nums):
        result = 0

        for num in nums:
            result ^= num

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.singleNumber([2, 2, 1])
    assert 4 == solution.singleNumber([4, 1, 2, 1, 2])
