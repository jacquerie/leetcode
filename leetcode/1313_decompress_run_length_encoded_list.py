# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            result.extend([nums[i + 1]] * nums[i])
        return result


if __name__ == '__main__':
    solution = Solution()

    assert [2, 4, 4, 4] == solution.decompressRLElist([1, 2, 3, 4])
