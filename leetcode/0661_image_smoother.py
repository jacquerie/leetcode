# -*- coding: utf-8 -*-

import itertools


class Solution:
    def imageSmoother(self, M):
        result = [[0 for j in range(len(M[0]))] for i in range(len(M))]

        for i in range(len(M)):
            for j in range(len(M[0])):
                count, partial = 0, 0
                for h, k in itertools.product([i - 1, i, i + 1], [j - 1, j, j + 1]):
                    if 0 <= h < len(M) and 0 <= k < len(M[0]):
                        partial += M[h][k]
                        count += 1
                result[i][j] = int(partial / count)

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ] == solution.imageSmoother([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ])
    assert [
        [4, 4, 5],
        [5, 6, 6],
        [8, 9, 9],
        [11, 12, 12],
        [13, 13, 14],
    ] == solution.imageSmoother([
        [2, 3, 4],
        [5, 6, 7],
        [8, 9, 10],
        [11, 12, 13],
        [14, 15, 16],
    ])
