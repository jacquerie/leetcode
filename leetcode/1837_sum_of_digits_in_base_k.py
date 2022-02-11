# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        return sum(self.toBaseK(n, k))

    def toBaseK(self, n: int, k: int) -> List[int]:
        digits = []
        while n:
            digits.append(n % k)
            n //= k
        return digits


if __name__ == "__main__":
    solution = Solution()

    assert 9 == solution.sumBase(34, 6)
    assert 1 == solution.sumBase(10, 10)
