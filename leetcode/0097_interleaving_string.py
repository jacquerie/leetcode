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
    def isInterleave(self, s1, s2, s3):
        return self._isInterleave(s1, s2, s3, 0, 0, 0)

    @memoize
    def _isInterleave(self, s1, s2, s3, i, j, k):
        if i == len(s1) and j == len(s2):
            return k == len(s3)
        elif k == len(s3):
            return i == len(s1) and j == len(s2)
        elif (i < len(s1) and s1[i] == s3[k]) and (j < len(s2) and s2[j] == s3[k]):
            return (
                self._isInterleave(s1, s2, s3, i + 1, j, k + 1) or
                self._isInterleave(s1, s2, s3, i, j + 1, k + 1)
            )
        elif i < len(s1) and s1[i] == s3[k]:
            return self._isInterleave(s1, s2, s3, i + 1, j, k + 1)
        elif j < len(s2) and s2[j] == s3[k]:
            return self._isInterleave(s1, s2, s3, i, j + 1, k + 1)
        return False


if __name__ == '__main__':
    solution = Solution()

    assert solution.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
    assert not solution.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')
    assert not solution.isInterleave('a', 'b', 'a')
