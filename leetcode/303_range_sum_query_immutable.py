# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class NumArray(object):
    def __init__(self, nums):
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, i, j):
        return self.sums[j + 1] - self.sums[i]


if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])

    assert 1 == obj.sumRange(0, 2)
    assert -1 == obj.sumRange(2, 5)
    assert -3 == obj.sumRange(0, 5)
