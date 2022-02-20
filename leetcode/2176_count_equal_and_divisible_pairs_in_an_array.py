# -*- coding: utf-8 -*-

from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        occurrences, result = defaultdict(list), 0
        for i, num in enumerate(nums):
            if num in occurrences:
                result += sum(i * j % k == 0 for j in occurrences[num])
            occurrences[num].append(i)
        return result


if __name__ == "__main__":
    solution = Solution()

    assert 4 == solution.countPairs([3, 1, 2, 2, 2, 1, 3], 2)
    assert 0 == solution.countPairs([1, 2, 3, 4], 1)
