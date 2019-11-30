# -*- coding: utf-8 -*-

import itertools


class Solution:
    def largestTriangleArea(self, points):
        result = 0

        for (x_a, y_a), (x_b, y_b), (x_c, y_c) in itertools.combinations(points, 3):
            area = abs((x_a - x_c) * (y_b - y_a) - (x_a - x_b) * (y_c - y_a)) / 2
            if area > result:
                result = area

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]])
    assert 0.5 == solution.largestTriangleArea([[1, 0], [0, 0], [0, 1]])
