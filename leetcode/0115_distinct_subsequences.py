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


class Solution(object):
    def numDistinct(self, s, t):
        return self._numDistinct(s, t, 0, 0)

    @memoize
    def _numDistinct(self, s, t, i, j):
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
