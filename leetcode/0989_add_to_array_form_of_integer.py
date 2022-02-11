# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return self.toArrayForm(self.fromArrayForm(num) + k)

    def toArrayForm(self, num: int) -> List[int]:
        return [int(digit) for digit in str(num)]

    def fromArrayForm(self, num: List[int]) -> int:
        result = 0
        for digit in num:
            result *= 10
            result += digit
        return result


if __name__ == "__main__":
    solution = Solution()

    assert [1, 2, 3, 4] == solution.addToArrayForm([1, 2, 0, 0], 34)
    assert [4, 5, 5] == solution.addToArrayForm([2, 7, 4], 181)
    assert [1, 0, 2, 1] == solution.addToArrayForm([2, 1, 5], 806)
    assert [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] == solution.addToArrayForm(
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1
    )
