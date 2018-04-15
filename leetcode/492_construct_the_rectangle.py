# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import math


class Solution(object):
    def constructRectangle(self, area):
        w = int(math.sqrt(area))
        while area % w:
            w -= 1
        return [area // w, w]


if __name__ == '__main__':
    solution = Solution()

    assert [2, 2] == solution.constructRectangle(4)
    assert [5, 1] == solution.constructRectangle(5)
    assert [3, 2] == solution.constructRectangle(6)
    assert [7, 1] == solution.constructRectangle(7)
    assert [4, 2] == solution.constructRectangle(8)
    assert [3, 3] == solution.constructRectangle(9)
