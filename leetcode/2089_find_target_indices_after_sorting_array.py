# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count_smaller, count_equal = 0, 0
        for num in nums:
            if num < target:
                count_smaller += 1
            elif num == target:
                count_equal += 1
        return list(range(count_smaller, count_smaller + count_equal))


if __name__ == "__main__":
    solution = Solution()

    assert [1, 2] == solution.targetIndices([1, 2, 5, 2, 3], 2)
    assert [3] == solution.targetIndices([1, 2, 5, 2, 3], 3)
    assert [4] == solution.targetIndices([1, 2, 5, 2, 3], 5)
