# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        current_index, current_min_distance = -1, float('inf')
        for index, (x1, y1) in enumerate(points):
            if x1 != x and y1 != y:
                continue
            distance = abs(x1 - x) + abs(y1 - y)
            if distance < current_min_distance:
                current_index, current_min_distance = index, distance
        return current_index


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.nearestValidPoint(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]])
    assert 0 == solution.nearestValidPoint(3, 4, [[3, 4]])
    assert -1 == solution.nearestValidPoint(3, 4, [[2, 3]])
