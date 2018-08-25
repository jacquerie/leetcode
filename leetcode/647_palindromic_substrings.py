# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def countSubstrings(self, s):
        return sum((el + 1) // 2 for el in self.manachersAlgorithm(s))

    def manachersAlgorithm(self, s):
        c, r = 0, 0
        s = '^#' + '#'.join(s) + '#$'
        p = [0] * len(s)

        for i in xrange(1, len(s) - 1):
            if i < r:
                p[i] = min(r - i, p[2 * c - i])
            while s[i + 1 + p[i]] == s[i - 1 - p[i]]:
                p[i] += 1
            if i + p[i] < r:
                c, r = i + p[i]

        return p


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.countSubstrings('abc')
    assert 6 == solution.countSubstrings('aaa')
