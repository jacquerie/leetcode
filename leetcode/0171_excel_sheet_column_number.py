# -*- coding: utf-8 -*-

import string


class Solution:
    def titleToNumber(self, s):
        result = 0

        for c in s:
            result *= 26
            result += string.ascii_uppercase.index(c) + 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.titleToNumber('A')
    assert 28 == solution.titleToNumber('AB')
    assert 701 == solution.titleToNumber('ZY')
