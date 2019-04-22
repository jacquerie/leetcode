# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools


class Solution(object):
    def permute(self, nums):
        return [list(el) for el in itertools.permutations(nums)]


if __name__ == '__main__':
    solution = Solution()

    assert [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ] == solution.permute([1, 2, 3])
