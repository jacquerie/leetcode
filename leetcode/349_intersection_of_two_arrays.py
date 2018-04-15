# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    solution = Solution()

    assert [2] == solution.intersection([1, 2, 2, 1], [2, 2])
