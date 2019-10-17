# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def queensAttacktheKing(self, queens, king):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        queens_set = set((x, y) for x, y in queens)

        result = []

        for dx, dy in directions:
            x, y = king
            while 0 <= x < 8 and 0 <= y < 8:
                x, y = x + dx, y + dy
                if (x, y) in queens_set:
                    result.append([x, y])
                    break

        return result


if __name__ == '__main__':
    solution = Solution()

    expected = [[0, 1], [1, 0], [3, 3]]
    result = solution.queensAttacktheKing([[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], [0, 0])

    assert sorted(expected) == sorted(result)

    expected = [[2, 2], [3, 4], [4, 4]]
    result = solution.queensAttacktheKing([[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]], [3, 3])

    assert sorted(expected) == sorted(result)

    expected = [[2, 3], [1, 4], [1, 6], [3, 7], [4, 3], [5, 4], [4, 5]]
    result = solution.queensAttacktheKing([[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4], [2, 2], [1, 1], [6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2], [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]], [3, 4])

    assert sorted(expected) == sorted(result)
