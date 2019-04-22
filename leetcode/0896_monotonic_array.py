# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def isMonotonic(self, A):
        decreasing, increasing = False, False
        for i in xrange(1, len(A)):
            if A[i] < A[i - 1] and not decreasing:
                decreasing = True
            elif A[i] > A[i - 1] and not increasing:
                increasing = True
        return not (decreasing and increasing)


if __name__ == '__main__':
    solution = Solution()

    assert solution.isMonotonic([1, 2, 2, 3])
    assert solution.isMonotonic([6, 5, 4, 4])
    assert not solution.isMonotonic([1, 3, 2])
    assert solution.isMonotonic([1, 2, 4, 5])
    assert solution.isMonotonic([1, 1, 1, 1])
