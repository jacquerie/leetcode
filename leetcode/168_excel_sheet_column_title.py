# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import string


class Solution(object):
    def convertToTitle(self, n):
        digits = []

        while n:
            digits.append(string.ascii_uppercase[(n - 1) % 26])
            n = (n - 1) // 26

        return ''.join(reversed(digits))


if __name__ == '__main__':
    solution = Solution()

    assert 'A' == solution.convertToTitle(1)
    assert 'AB' == solution.convertToTitle(28)
    assert 'ZY' == solution.convertToTitle(701)
