# -*- coding: utf-8 -*-

from functools import wraps


def memoize(f):
    cache = f.cache = {}

    @wraps(f)
    def _memoize(*args, **kwargs):
        if args not in cache:
            cache[args] = f(*args, **kwargs)
        return cache[args]
    return _memoize


class Solution:
    def checkValidString(self, s):
        return self._checkValidString(s, 0, 0)

    @memoize
    def _checkValidString(self, s, i, c):
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
