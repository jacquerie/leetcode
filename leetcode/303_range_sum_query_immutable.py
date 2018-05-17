# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class NumArray(object):
    def __init__(self, nums):
        current, self.sums = 0, []
        for num in nums:
            current += num
            self.sums.append(current)

    def sumRange(self, i, j):
        if i:
            return self.sums[j] - self.sums[i - 1]
        return self.sums[j]


if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])

    assert 1 == obj.sumRange(0, 2)
    assert -1 == obj.sumRange(2, 5)
    assert -3 == obj.sumRange(0, 5)
