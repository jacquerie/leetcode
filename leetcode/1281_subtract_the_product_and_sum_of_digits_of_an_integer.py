# -*- coding: utf-8 -*-

from math import prod
from typing import List


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = self.getDigits(n)
        return prod(digits) - sum(digits)

    def getDigits(self, n: int) -> List[int]:
        digits = []
        while n:
            digits.append(n % 10)
            n //= 10
        return digits


if __name__ == '__main__':
    solution = Solution()

    assert 15 == solution.subtractProductAndSum(234)
    assert 21 == solution.subtractProductAndSum(4421)
