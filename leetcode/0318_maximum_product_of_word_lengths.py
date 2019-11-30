# -*- coding: utf-8 -*-

import itertools


class Solution:
    def maxProduct(self, words):
        lengths = [len(word) for word in words]

        bits = [0] * len(words)
        for i, word in enumerate(words):
            for c in word:
                bits[i] |= 1 << (ord(c) - ord('a'))

        result = 0

        for i, j in itertools.combinations(range(len(words)), 2):
            if lengths[i] * lengths[j] > result and not bits[i] & bits[j]:
                result = lengths[i] * lengths[j]

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 16 == solution.maxProduct(['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef'])
    assert 4 == solution.maxProduct(['a', 'ab', 'abc', 'd', 'cd', 'bcd', 'abcd'])
    assert 0 == solution.maxProduct(['a', 'aa', 'aaa', 'aaaa'])
