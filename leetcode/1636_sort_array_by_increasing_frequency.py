# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        return sorted(nums, key=lambda el: (counts[el], -el))


if __name__ == "__main__":
    solution = Solution()

    assert [3, 1, 1, 2, 2, 2] == solution.frequencySort([1, 1, 2, 2, 2, 3])
    assert [1, 3, 3, 2, 2] == solution.frequencySort([2, 3, 1, 3, 2])
    assert [5, -1, 4, 4, -6, -6, 1, 1, 1] == solution.frequencySort(
        [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    )
