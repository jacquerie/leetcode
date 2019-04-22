# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def rob(self, nums):
        current, previous = 0, 0

        for num in nums:
            current, previous = max(previous + num, current), current

        return current


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.rob([1, 2, 3, 1])
    assert 12 == solution.rob([2, 7, 9, 3, 1])
