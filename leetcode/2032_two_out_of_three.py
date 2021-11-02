# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        counts = Counter()
        for el in set(nums1):
            counts[el] += 1
        for el in set(nums2):
            counts[el] += 1
        for el in set(nums3):
            counts[el] += 1
        return [k for k, v in counts.items() if v >= 2]


if __name__ == '__main__':
    solution = Solution()

    assert [2, 3] == solution.twoOutOfThree([1, 1, 3, 2], [2, 3], [3])
    assert [1, 3, 2] == solution.twoOutOfThree([3, 1], [2, 3], [1, 2])
    assert [] == solution.twoOutOfThree([1, 2, 2], [4, 3, 3], [5])
