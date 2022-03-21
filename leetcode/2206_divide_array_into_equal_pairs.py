# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(el % 2 == 0 for el in Counter(nums).values())


if __name__ == "__main__":
    solution = Solution()

    assert solution.divideArray([3, 2, 3, 2, 2, 2])
    assert not solution.divideArray([1, 2, 3, 4])
