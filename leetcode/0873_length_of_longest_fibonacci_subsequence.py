# -*- coding: utf-8 -*-

import itertools


class Solution:
    def lenLongestFibSubseq(self, A):
        result = 2

        A_set = set(A)
        for x, y in itertools.combinations(A, 2):
            partial = 2
            while x + y in A_set:
                x, y = y, x + y
                partial += 1
            result = max(result, partial)

        return result if result > 2 else 0


if __name__ == "__main__":
    solution = Solution()

    assert 5 == solution.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8])
    assert 3 == solution.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18])
