# -*- coding: utf-8 -*-

import math


class Solution:
    def bulbSwitch(self, n):
        return int(math.sqrt(n))


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.bulbSwitch(3)
