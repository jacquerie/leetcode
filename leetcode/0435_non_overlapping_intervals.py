# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])

        current_end, result = float('-inf'), 0
        for interval in intervals:
            if interval[0] >= current_end:
                current_end = interval[1]
            else:
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
    assert 2 == solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]])
    assert 0 == solution.eraseOverlapIntervals([[1, 2], [2, 3]])
