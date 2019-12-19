# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        current, result = 0, 0

        intervals.sort(key=lambda el: (el[0], -el[1]))
        for _, end in intervals:
            if end > current:
                result += 1
            current = max(current, end)

        return result


if __name__ == '__solution__':
    solution = Solution()

    assert 2 == solution.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]])
