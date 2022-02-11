# -*- coding: utf-8 -*-

import math


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n + 4, n)


if __name__ == "__main__":
    solution = Solution()

    assert 5 == solution.countVowelStrings(1)
    assert 15 == solution.countVowelStrings(2)
    assert 66045 == solution.countVowelStrings(33)
