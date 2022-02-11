# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        result = 0

        counts = Counter(el % 60 for el in time)
        for el, count in counts.items():
            if el == 0 or el == 30:
                result += count * (count - 1)
            else:
                result += count * counts[60 - el]

        return result // 2


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.numPairsDivisibleBy60([30, 20, 150, 100, 40])
    assert 3 == solution.numPairsDivisibleBy60([60, 60, 60])
