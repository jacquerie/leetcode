# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True

        i = 0
        for c in t:
            if i < len(s) and c == s[i]:
                i += 1

        return i == len(s)


if __name__ == '__main__':
    solution = Solution()

    assert solution.isSubsequence('abc', 'ahbgdc')
    assert not solution.isSubsequence('axc', 'ahbgdc')
    assert solution.isSubsequence('', 'ahbgdc')
    assert solution.isSubsequence('a', 'ab')
