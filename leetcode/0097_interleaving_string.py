# -*- coding: utf-8 -*-

from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self._isInterleave(s1, s2, s3, 0, 0, 0)

    @lru_cache(maxsize=None)
    def _isInterleave(self, s1: str, s2: str, s3: str, i: int, j: int, k: int) -> bool:
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
