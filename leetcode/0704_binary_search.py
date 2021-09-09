# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums) - 1
        while first <= last:
            mid = first + (last - first) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                last = mid - 1
            else:
                first = mid + 1
        return -1


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.search([-1, 0, 3, 5, 9, 12], 9)
    assert -1 == solution.search([-1, 0, 3, 5, 9, 12], 2)
