# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(el for el, count in Counter(nums).items() if count == 1)


if __name__ == "__main__":
    solution = Solution()

    assert 4 == solution.sumOfUnique([1, 2, 3, 2])
    assert 0 == solution.sumOfUnique([1, 1, 1, 1, 1])
    assert 15 == solution.sumOfUnique([1, 2, 3, 4, 5])
