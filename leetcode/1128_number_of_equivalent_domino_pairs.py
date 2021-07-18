# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = Counter()
        for domino in dominoes:
            normalized_domino = tuple(sorted(domino))
            counts[normalized_domino] += 1

        return sum(count * (count - 1) // 2 for count in counts.values())


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]])
