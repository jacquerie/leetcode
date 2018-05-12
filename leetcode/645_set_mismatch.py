# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def findErrorNums(self, nums):
        repeated = (Counter(nums) - Counter(range(1, len(nums) + 1))).keys()
        missing = list(set(range(1, len(nums) + 1)) - set(nums))

        return repeated + missing


if __name__ == '__main__':
    solution = Solution()

    assert [2, 3] == solution.findErrorNums([1, 2, 2, 4])
