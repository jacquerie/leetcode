# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools


class Solution(object):
    def subsets(self, nums):
        return list(itertools.chain.from_iterable(
            (list(el) for el in itertools.combinations(nums, n)) for n in xrange(len(nums) + 1)))


if __name__ == '__main__':
    solution = Solution()

    assert [
        [],
        [1],
        [2],
        [3],
        [1, 2],
        [1, 3],
        [2, 3],
        [1, 2, 3],
    ] == solution.subsets([1, 2, 3])
