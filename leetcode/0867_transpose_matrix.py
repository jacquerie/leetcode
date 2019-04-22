# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def transpose(self, A):
        return [[A[j][i] for j in xrange(len(A))] for i in xrange(len(A[0]))]


if __name__ == '__main__':
    solution = Solution()

    assert [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ] == solution.transpose([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])
