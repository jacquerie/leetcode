# -*- coding: utf-8 -*-

from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self._numDistinct(s, t, 0, 0)

    @lru_cache(maxsize=None)
    def _numDistinct(self, s: str, t: str, i: int, j: int) -> bool:
        if i == len(s) and j < len(t):
            return 0
        elif j == len(t):
            return 1
        elif s[i] == t[j]:
            return self._numDistinct(s, t, i + 1, j) +\
                self._numDistinct(s, t, i + 1, j + 1)
        return self._numDistinct(s, t, i + 1, j)


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.numDistinct('rabbbit', 'rabbit')
    assert 5 == solution.numDistinct('babgbag', 'bag')
