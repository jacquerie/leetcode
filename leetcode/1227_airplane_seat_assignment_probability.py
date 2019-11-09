# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        return 1 if n == 1 else 0.5


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.nthPersonGetsNthSeat(1)
    assert 0.5 == solution.nthPersonGetsNthSeat(2)
    assert 0.5 == solution.nthPersonGetsNthSeat(3)
