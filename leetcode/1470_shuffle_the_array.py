# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [(nums[i // 2] if i % 2 == 0 else nums[i // 2 + n]) for i in range(2 * n)]


if __name__ == '__main__':
    solution = Solution()

    assert [2, 3, 5, 4, 1, 7] == solution.shuffle([2, 5, 1, 3, 4, 7], 3)
    assert [1, 4, 2, 3, 3, 2, 4, 1] == solution.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4)
    assert [1, 2, 1, 2] == solution.shuffle([1, 1, 2, 2], 2)
