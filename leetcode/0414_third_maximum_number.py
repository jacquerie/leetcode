# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def thirdMax(self, nums):
        top = [float('-inf'), float('-inf'), float('-inf')]

        for num in nums:
            if num > top[0]:
                top[0], top[1], top[2] = num, top[0], top[1]
            elif num != top[0] and num > top[1]:
                top[1], top[2] = num, top[1]
            elif num != top[0] and num != top[1] and num > top[2]:
                top[2] = num

        if any(el == float('-inf') for el in top):
            return top[0]
        return top[2]


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.thirdMax([3, 2, 1])
    assert 2 == solution.thirdMax([1, 2])
    assert 1 == solution.thirdMax([2, 2, 3, 1])
