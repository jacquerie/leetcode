# -*- coding: utf-8 -*-


class Solution:
    def convertToBase7(self, num):
        if num == 0:
            return '0'

        sign = -1 if num < 0 else 1

        num *= sign
        digits = []

        while num:
            digits.append(str(num % 7))
            num //= 7

        if sign < 0:
            digits.append('-')

        return ''.join(reversed(digits))


if __name__ == '__main__':
    solution = Solution()

    assert '202' == solution.convertToBase7(100)
    assert '-10' == solution.convertToBase7(-7)
