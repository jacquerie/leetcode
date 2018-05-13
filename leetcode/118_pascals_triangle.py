# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        result = [
            [1],
            [1, 1],
        ]

        for i in range(2, numRows):
            partial = [1] + [result[-1][j - 1] + result[-1][j] for j in range(1, i)] + [1]
            result.append(partial)

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [
       [1],
       [1, 1],
       [1, 2, 1],
       [1, 3, 3, 1],
       [1, 4, 6, 4, 1],
    ] == solution.generate(5)
