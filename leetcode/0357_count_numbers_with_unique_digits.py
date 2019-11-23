# -*- coding: utf-8 -*-


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n > 10:
            return 0
        elif 1 <= n <= 10:
            return 9 * self.factorialPrefix(9, n - 1) + self.countNumbersWithUniqueDigits(n - 1)
        return 1

    def factorialPrefix(self, m, n):
        result = 1
        while n:
            result *= m
            m -= 1
            n -= 1
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 91 == solution.countNumbersWithUniqueDigits(2)
