# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts, current_sum = Counter(arr), 0
        for i, (_, count) in enumerate(counts.most_common(), 1):
            current_sum += count
            if current_sum >= len(arr) // 2:
                return i


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7])
    assert 1 == solution.minSetSize([7, 7, 7, 7, 7, 7])
    assert 1 == solution.minSetSize([1, 9])
    assert 1 == solution.minSetSize([1000, 1000, 3, 7])
    assert 5 == solution.minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
