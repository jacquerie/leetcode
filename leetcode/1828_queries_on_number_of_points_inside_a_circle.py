# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        return [sum((xi - xj) ** 2 + (yi - yj) ** 2 <= rj ** 2 for xi, yi in points) for xj, yj, rj in queries]


if __name__ == '__main__':
    solution = Solution()

    assert [3, 2, 2] == solution.countPoints([[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]])
    assert [2, 3, 2, 4] == solution.countPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]])
