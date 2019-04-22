# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import re


class Solution(object):
    def maskPII(self, S):
        if self.isEmail(S):
            return self.maskEmail(S)
        return self.maskPhoneNumber(S)

    def isEmail(self, S):
        return '@' in S

    def maskEmail(self, S):
        name1, rest = S.lower().split('@')
        return '@'.join([name1[0] + ('*' * 5) + name1[-1], rest])

    def maskPhoneNumber(self, S):
        S = re.sub(r'\(|\)|\+|\-|\ ', '', S)
        prefixLength = len(S) - 10
        if prefixLength:
            return '-'.join(['+' + '*' * prefixLength, '*' * 3, '*' * 3, S[-4:]])
        return '-'.join(['*' * 3, '*' * 3, S[-4:]])


if __name__ == '__main__':
    solution = Solution()

    assert 'l*****e@leetcode.com' == solution.maskPII('LeetCode@LeetCode.com')
    assert 'a*****b@qq.com' == solution.maskPII('AB@qq.com')
    assert '***-***-7890' == solution.maskPII('1(234)567-890')
    assert '+**-***-***-5678' == solution.maskPII('86-(10)12345678')
