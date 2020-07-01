# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], indices: List[int]) -> List[int]:
        result = []
        for index, num in zip(indices, nums):
            result.insert(index, num)
        return result


if __name__ == '__main__':
    solution = Solution()

    assert [0, 4, 1, 3, 2] == solution.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1])
    assert [0, 1, 2, 3, 4] == solution.createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 3, 0])
    assert [1] == solution.createTargetArray([1], [0])
