# -*- coding: utf-8 -*-

from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return N

        trust_dict = defaultdict(int)
        for a, b in trust:
            trust_dict[a] -= 1
            trust_dict[b] += 1

        for el, count in trust_dict.items():
            if count == N - 1:
                return el

        return -1


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.findJudge(2, [[1, 2]])
    assert 3 == solution.findJudge(3, [[1, 3], [2, 3]])
    assert -1 == solution.findJudge(3, [[1, 3], [2, 3], [3, 1]])
    assert -1 == solution.findJudge(3, [[1, 2], [2, 3]])
    assert 3 == solution.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])
