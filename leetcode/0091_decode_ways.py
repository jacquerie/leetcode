# -*- coding: utf-8 -*-

from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        return self._numDecodings(s, 0)

    @lru_cache(maxsize=None)
    def _numDecodings(self, s: str, i: int) -> int:
        if i > len(s):
            return 0
        elif i == len(s):
            return 1
        elif s[i] == '0':
            return 0
        elif s[i] == '1':
            return self._numDecodings(s, i + 1) + self._numDecodings(s, i + 2)
        elif s[i] == '2':
            if i + 1 < len(s) and 0 <= int(s[i + 1]) < 7:
                return self._numDecodings(s, i + 1) + self._numDecodings(s, i + 2)
        return self._numDecodings(s, i + 1)


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.numDecodings('12')
    assert 3 == solution.numDecodings('226')
    assert 0 == solution.numDecodings('0')
