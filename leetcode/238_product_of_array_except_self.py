# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools


class Solution(object):
    def productExceptSelf(self, nums):
        left_products = [1]
        for i in range(len(nums) - 1):
            left_products.append(left_products[-1] * nums[i])

        right_products = [1]
        for i in range(len(nums) - 1, 0, -1):
            right_products.append(right_products[-1] * nums[i])

        return [l * r for l, r in itertools.izip(left_products, reversed(right_products))]


if __name__ == '__main__':
    solution = Solution()

    assert [24, 12, 8, 6] == solution.productExceptSelf([1, 2, 3, 4])
