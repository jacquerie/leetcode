# -*- coding: utf-8 -*-


class Solution:
    def checkStraightLine(self, coordinates):
        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]

        m = (y1 - y0) / (x1 - x0) if x1 != x0 else 0
        q = y0 - m * x0

        return all(y == m * x + q for x, y in coordinates)


if __name__ == '__main__':
    solution = Solution()

    assert solution.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    assert not solution.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])
