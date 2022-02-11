# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        nums[::2] = sorted(nums[::2])
        nums[1::2] = sorted(nums[1::2], reverse=True)

        return nums


if __name__ == "__main__":
    solution = Solution()

    assert [2, 3, 4, 1] == solution.sortEvenOdd([4, 1, 2, 3])
    assert [2, 1] == solution.sortEvenOdd([2, 1])
