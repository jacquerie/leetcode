# -*- coding: utf-8 -*-


class Solution(object):
    def findNthDigit(self, n):
        digits = 1
        while n > 9 * digits * (10 ** (digits - 1)):
            n -= 9 * digits * (10 ** (digits - 1))
            digits += 1

        num = str(10 ** (digits - 1) + (n - 1) // digits)
        digit = (n - 1) % digits

        return int(num[digit])


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.findNthDigit(3)
    assert 0 == solution.findNthDigit(11)
    assert 9 == solution.findNthDigit(9)
    assert 3 == solution.findNthDigit(1000)
