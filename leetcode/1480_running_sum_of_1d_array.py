# -*- coding: utf-8 -*-

import itertools
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(itertools.accumulate(nums))


if __name__ == "__main__":
    solution = Solution()

    assert [1, 3, 6, 10] == solution.runningSum([1, 2, 3, 4])
    assert [1, 2, 3, 4, 5] == solution.runningSum([1, 1, 1, 1, 1])
    assert [3, 4, 6, 16, 17] == solution.runningSum([3, 1, 2, 10, 1])
