# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        return list((Counter(nums1) & Counter(nums2)).elements())


if __name__ == '__main__':
    solution = Solution()

    assert [2, 2] == solution.intersect([1, 2, 2, 1], [2, 2])
