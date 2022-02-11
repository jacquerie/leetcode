# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(count * (count - 1) // 2 for _, count in Counter(nums).items())


if __name__ == "__main__":
    solution = Solution()

    assert 4 == solution.numIdenticalPairs([1, 2, 3, 1, 1, 3])
    assert 6 == solution.numIdenticalPairs([1, 1, 1, 1])
    assert 0 == solution.numIdenticalPairs([1, 2, 3])
