# -*- coding: utf-8 -*-

from collections import Counter


class Solution(object):
    def oddCells(self, n, m, indices):
        row_counts = Counter()
        col_counts = Counter()
        for row, col in indices:
            row_counts[row] += 1
            col_counts[col] += 1

        return sum((row_counts[i] + col_counts[j]) % 2 for i in range(n) for j in range(m))


if __name__ == '__main__':
    solution = Solution()

    assert 6 == solution.oddCells(2, 3, [[0, 1], [1, 1]])
    assert 0 == solution.oddCells(2, 2, [[1, 1], [0, 0]])
