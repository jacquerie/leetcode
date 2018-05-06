# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def largestTriangleArea(self, points):
        result = 0

        for i in range(len(points)):
            for j in range(i, len(points)):
                for k in range(j, len(points)):
                    x_a, y_a = points[i]
                    x_b, y_b = points[j]
                    x_c, y_c = points[k]

                    area = abs((x_a - x_c) * (y_b - y_a) - (x_a - x_b) * (y_c - y_a)) / 2
                    if area > result:
                        result = area

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]])
    assert 0.5 == solution.largestTriangleArea([[1,0],[0,0],[0,1]])
