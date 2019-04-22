# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def minFallingPathSum(self, A):
        result = [[0 for j in xrange(len(A[0]))] for i in xrange(len(A))]

        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                if i == 0:
                    result[i][j] = A[i][j]
                elif j == 0:
                    result[i][j] = A[i][j] + min(result[i - 1][j], result[i - 1][j + 1])
                elif j == len(A[0]) - 1:
                    result[i][j] = A[i][j] + min(result[i - 1][j - 1], result[i - 1][j])
                else:
                    result[i][j] = A[i][j] + min(
                        result[i - 1][j - 1], result[i - 1][j], result[i - 1][j + 1])

        return min(result[-1])


if __name__ == '__main__':
    solution = Solution()

    assert 12 == solution.minFallingPathSum([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])
