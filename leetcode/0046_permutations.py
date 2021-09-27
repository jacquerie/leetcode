# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self._permute(nums, [], result)
        return result

    def _permute(self, nums: List[int], current: List[int], result: List[List[int]]):
        if not nums:
            result.append(current)
        for i in range(len(nums)):
            self._permute(nums[:i] + nums[i + 1:], current + [nums[i]], result)


if __name__ == '__main__':
    solution = Solution()

    assert [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ] == solution.permute([1, 2, 3])
    assert [[0, 1], [1, 0]] == solution.permute([0, 1])
    assert [[1]] == solution.permute([1])
