# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        index = {}
        for i, num in enumerate(sorted(nums)):
            if num not in index:
                index[num] = i

        return [index[num] for num in nums]


if __name__ == "__main__":
    solution = Solution()

    assert [4, 0, 1, 1, 3] == solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3])
    assert [2, 1, 0, 3] == solution.smallerNumbersThanCurrent([6, 5, 4, 8])
    assert [0, 0, 0, 0] == solution.smallerNumbersThanCurrent([7, 7, 7, 7])
