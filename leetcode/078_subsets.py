# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def subsets(self, nums):
        result = []
        self._subsets(nums, [], result)
        return result

    def _subsets(self, nums, current, result):
        if not nums:
            if current not in result:
                result.append(current)
        else:
            self._subsets(nums[1:], current, result)
            self._subsets(nums[1:], current + [nums[0]], result)


if __name__ == '__main__':
    solution = Solution()

    assert [
        [],
        [3],
        [2],
        [2, 3],
        [1],
        [1, 3],
        [1, 2],
        [1, 2, 3],
    ] == solution.subsets([1, 2, 3])
