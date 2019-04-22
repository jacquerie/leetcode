# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def hammingDistance(self, x, y):
        xs = format(x, '032b')
        ys = format(y, '032b')

        return sum(xc != yc for xc, yc in zip(xs, ys))


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.hammingDistance(1, 4)
