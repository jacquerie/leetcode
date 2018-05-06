# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def rotateString(self, A, B):
        return len(A) == len(B) and B in A * 2


if __name__ == '__main__':
    solution = Solution()

    assert solution.rotateString('abcde', 'cdeab')
    assert not solution.rotateString('abcde', 'abced')
    assert not solution.rotateString('aa', 'a')
