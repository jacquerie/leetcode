# -*- coding: utf-8 -*-

import itertools
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        return sum(a + b + c == d for a, b, c, d in itertools.combinations(nums, 4))


if __name__ == "__main__":
    solution = Solution()

    assert 1 == solution.countQuadruplets([1, 2, 3, 6])
    assert 0 == solution.countQuadruplets([3, 3, 6, 4, 5])
    assert 4 == solution.countQuadruplets([1, 1, 1, 3, 5])
