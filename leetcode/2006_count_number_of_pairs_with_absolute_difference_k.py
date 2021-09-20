# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counts, result = Counter(nums), 0
        for num, count in counts.items():
            result += count * counts.get(num + k, 0)
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.countKDifference([1, 2, 2, 1], 1)
    assert 0 == solution.countKDifference([1, 3], 3)
    assert 3 == solution.countKDifference([3, 2, 1, 5, 4], 2)
