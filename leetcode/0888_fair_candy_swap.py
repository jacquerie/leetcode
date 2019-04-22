# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def fairCandySwap(self, A, B):
        difference = (sum(A) - sum(B)) // 2
        setB = set(B)

        for a in A:
            if a - difference in setB:
                return [a, a - difference]


if __name__ == '__main__':
    solution = Solution()

    assert [1, 2] == solution.fairCandySwap([1, 1], [2, 2])
    assert [1, 2] == solution.fairCandySwap([1, 2], [2, 3])
    assert [2, 3] == solution.fairCandySwap([2], [1, 3])
    assert [5, 4] == solution.fairCandySwap([1, 2, 5], [2, 4])
