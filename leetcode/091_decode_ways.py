# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

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
    def numDecodings(self, s):
        return self._numDecodings(s, 0)

    @memoize
    def _numDecodings(self, s, i):
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
