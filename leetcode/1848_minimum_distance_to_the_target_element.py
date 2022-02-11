# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min(abs(i - start) for i, el in enumerate(nums) if el == target)


if __name__ == "__main__":
    solution = Solution()

    assert 1 == solution.getMinDistance([1, 2, 3, 4, 5], 5, 3)
    assert 0 == solution.getMinDistance([1], 1, 0)
    assert 0 == solution.getMinDistance([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0)
