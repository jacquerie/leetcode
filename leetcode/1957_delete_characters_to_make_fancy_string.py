# -*- coding: utf-8 -*-

import itertools


class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for char, group in itertools.groupby(s):
            length = len(list(group))
            result.extend([char] * min(length, 2))
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()

    assert 'leetcode' == solution.makeFancyString('leeetcode')
    assert 'aabaa' == solution.makeFancyString('aaabaaaa')
    assert 'aab' == solution.makeFancyString('aab')
