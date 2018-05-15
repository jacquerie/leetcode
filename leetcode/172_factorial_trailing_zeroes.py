# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def trailingZeroes(self, n):
        result = 0

        i, powers = 1, []
        while 5 ** i <= n:
            powers.append(5 ** i)
            i += 1

        for power in powers:
            result += int(n / power)

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 0 == solution.trailingZeroes(3)
    assert 1 == solution.trailingZeroes(5)
    assert 24 == solution.trailingZeroes(100)
