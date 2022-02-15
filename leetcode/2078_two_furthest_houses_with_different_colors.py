# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        result = float("-inf")

        for i, color in enumerate(colors):
            if color != colors[0]:
                result = max(result, i)
            if color != colors[-1]:
                result = max(result, len(colors) - i - 1)

        return result


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.maxDistance([1, 1, 1, 6, 1, 1, 1])
    assert 4 == solution.maxDistance([1, 8, 3, 8, 3])
    assert 1 == solution.maxDistance([0, 1])
