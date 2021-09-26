# -*- coding: utf-8 -*-

from functools import lru_cache


class Solution:
    def checkValidString(self, s: str) -> bool:
        return self._checkValidString(s, 0, 0)

    @lru_cache(maxsize=None)
    def _checkValidString(self, s: str, i: int, c: int) -> bool:
        if i == len(s):
            return c == 0
        elif c < 0:
            return False
        elif s[i] == '(':
            return self._checkValidString(s, i + 1, c + 1)
        elif s[i] == ')':
            return self._checkValidString(s, i + 1, c - 1)
        return (
            self._checkValidString(s, i + 1, c - 1) or
            self._checkValidString(s, i + 1, c) or
            self._checkValidString(s, i + 1, c + 1)
        )


if __name__ == '__main__':
    solution = Solution()

    assert solution.checkValidString('()')
    assert solution.checkValidString('(*)')
    assert solution.checkValidString('(*))')
