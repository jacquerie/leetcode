# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools


class Solution(object):
    def maxProduct(self, words):
        lengths = [None] * len(words)
        for i, word in enumerate(words):
            lengths[i] = len(word)

        sets = [None] * len(words)
        for i, word in enumerate(words):
            sets[i] = set(word)

        result = 0

        for i, j in itertools.combinations(xrange(len(words)), 2):
            if lengths[i] * lengths[j] > result and not sets[i] & sets[j]:
                result = lengths[i] * lengths[j]

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 16 == solution.maxProduct(['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef'])
    assert 4 == solution.maxProduct(['a', 'ab', 'abc', 'd', 'cd', 'bcd', 'abcd'])
    assert 0 == solution.maxProduct(['a', 'aa', 'aaa', 'aaaa'])
