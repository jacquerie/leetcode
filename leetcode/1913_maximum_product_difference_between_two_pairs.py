# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a, b, c, d = float("-inf"), float("-inf"), float("inf"), float("inf")

        for num in nums:
            if num > a:
                a, b = num, a
            elif num > b:
                b = num
            if num < d:
                d, c = num, d
            elif num < c:
                c = num

        return a * b - c * d


if __name__ == "__main__":
    solution = Solution()

    assert 34 == solution.maxProductDifference([5, 6, 2, 7, 4])
    assert 64 == solution.maxProductDifference([4, 2, 5, 9, 7, 4, 8])
