# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def findComplement(self, num):
        return int(''.join('1' if digit == '0' else '0' for digit in format(num, '32b')), 2)


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.findComplement(5)
    assert 0 == solution.findComplement(1)
