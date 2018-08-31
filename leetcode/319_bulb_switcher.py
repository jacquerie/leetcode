# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import math


class Solution(object):
    def bulbSwitch(self, n):
        return int(math.sqrt(n))


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.bulbSwitch(3)
