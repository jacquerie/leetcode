# -*- coding: utf-8 -*-

import itertools
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return max((x - 1) * (y - 1) for x, y in itertools.combinations(nums, 2))


if __name__ == "__main__":
    solution = Solution()

    assert 12 == solution.maxProduct([3, 4, 5, 2])
    assert 16 == solution.maxProduct([1, 5, 4, 5])
    assert 12 == solution.maxProduct([3, 7])
