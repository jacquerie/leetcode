# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counter = Counter(
            nums[i + 1] for i in range(0, len(nums) - 1) if nums[i] == key
        )
        most_frequent, _ = counter.most_common(1)[0]

        return most_frequent


if __name__ == "__main__":
    solution = Solution()

    assert 100 == solution.mostFrequent([1, 100, 200, 1, 100], 1)
    assert 2 == solution.mostFrequent([2, 2, 2, 2, 3], 2)
