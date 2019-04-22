# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools


class Solution(object):
    def addStrings(self, num1, num2):
        def toInt(c):
            if c is None:
                return 0
            return int(c)

        result = []

        carry = 0
        for d1, d2 in itertools.izip_longest(reversed(num1), reversed(num2)):
            carry, digit = divmod(toInt(d1) + toInt(d2) + carry, 10)
            result.append(str(digit))
        if carry:
            result.append(str(carry))

        return ''.join(reversed(result))


if __name__ == '__main__':
    solution = Solution()

    assert '18' == solution.addStrings('9', '9')
    assert '28' == solution.addStrings('9', '19')
