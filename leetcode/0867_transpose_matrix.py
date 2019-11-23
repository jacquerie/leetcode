# -*- coding: utf-8 -*-


class Solution(object):
    def transpose(self, A):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


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
