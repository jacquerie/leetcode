# -*- coding: utf-8 -*-


class Solution:
    def minTimeToVisitAllPoints(self, points):
        result = 0
        for i in range(len(points) - 1):
            result += self.distance(points[i], points[i + 1])
        return result

    def distance(self, p1, p2):
        dx = abs(p1[0] - p2[0])
        dy = abs(p1[1] - p2[1])
        return min(dx, dy) + abs(dx - dy)


if __name__ == '__main__':
    solution = Solution()

    assert 7 == solution.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]])
    assert 5 == solution.minTimeToVisitAllPoints([[3, 2], [-2, 2]])
