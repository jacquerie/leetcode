# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        return list((Counter(nums1) & Counter(nums2)).elements())


if __name__ == '__main__':
    solution = Solution()

    assert [2, 2] == solution.intersect([1, 2, 2, 1], [2, 2])
