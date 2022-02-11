# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)


if __name__ == "__main__":
    solution = Solution()

    assert solution.canBeEqual([1, 2, 3, 4], [2, 4, 1, 3])
    assert solution.canBeEqual([7], [7])
    assert solution.canBeEqual([1, 12], [12, 1])
    assert not solution.canBeEqual([3, 7, 9], [3, 7, 11])
    assert solution.canBeEqual([1, 1, 1, 1, 1], [1, 1, 1, 1, 1])
