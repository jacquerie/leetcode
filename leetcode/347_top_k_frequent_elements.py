# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        return [k for k, v in Counter(nums).most_common(k)]


if __name__ == '__main__':
    solution = Solution()

    assert [1, 2] == solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
