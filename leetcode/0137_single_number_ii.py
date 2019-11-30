# -*- coding: utf-8 -*-

import itertools


class Solution:
    def fromBase3(self, digits):
        return int(''.join(str(digit) for digit in reversed(digits)), 3)

    def sumBase3(self, digits):
        return sum(digit for digit in digits if digit) % 3

    def toBase3(self, num):
        digits = []
        while num:
            digits.append(num % 3)
            num //= 3
        return digits

    def singleNumber(self, nums):
        min_num = min(nums)
        nums = [num + abs(min_num) for num in nums]

        nums_in_base3 = [self.toBase3(num) for num in nums]
        sums_in_base3 = [self.sumBase3(el) for el in itertools.zip_longest(*nums_in_base3)]

        return self.fromBase3(sums_in_base3) - abs(min_num)


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.singleNumber([2, 2, 3, 2])
    assert 99 == solution.singleNumber([0, 1, 0, 1, 0, 1, 99])
    assert -4 == solution.singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2])
