# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indices_of_top_k_nums = sorted(enumerate(nums), key=lambda el: -el[1])[:k]
        sorted_indices_of_top_k_nums = sorted(indices_of_top_k_nums)
        return [num for index, num in sorted_indices_of_top_k_nums]


if __name__ == "__main__":
    solution = Solution()

    assert [3, 3] == solution.maxSubsequence([2, 1, 3, 3], 2)
    assert [-1, 3, 4] == solution.maxSubsequence([-1, -2, 3, 4], 3)
    assert [3, 4] == solution.maxSubsequence([3, 4, 3, 3], 2)
