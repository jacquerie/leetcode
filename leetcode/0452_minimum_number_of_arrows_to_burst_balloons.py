# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[1])

        current_end, result = float("-inf"), len(points)
        for point in points:
            if point[0] > current_end:
                current_end = point[1]
            else:
                result -= 1
        return result


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])
    assert 4 == solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]])
    assert 2 == solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]])
