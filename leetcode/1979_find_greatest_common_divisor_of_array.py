# -*- coding: utf-8 -*-

import math
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(min(nums), max(nums))


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.findGCD([2, 5, 6, 9, 10])
    assert 1 == solution.findGCD([7, 5, 6, 8, 3])
    assert 3 == solution.findGCD([3, 3])
