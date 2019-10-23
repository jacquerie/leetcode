# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def findErrorNums(self, nums):
        result = []

        for num in nums:
            i = abs(num) - 1
            if nums[i] < 0:
                result.append(i + 1)
            nums[i] = -nums[i]

        for i, num in enumerate(nums, 1):
            if num > 0 and i not in result:
                result.append(i)
                break

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [2, 3] == solution.findErrorNums([1, 2, 2, 4])
    assert [2, 1] == solution.findErrorNums([2, 2])
