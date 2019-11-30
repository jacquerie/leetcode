# -*- coding: utf-8 -*-

import itertools


class Solution:
    def reverseStr(self, s, k):
        result = []

        for chunk in self.chunkStr(s, 2 * k):
            result.append(reversed(chunk[:k]))
            result.append(chunk[k:])

        return ''.join(self.flattenLst(result))

    def chunkStr(self, s, k):
        for i in range((len(s) // k) + 1):
            start, end = k * i, k * i + k
            yield s[start:end]

    def flattenLst(self, l):
        return itertools.chain.from_iterable(l)


if __name__ == '__main__':
    solution = Solution()

    assert 'bacdfeg' == solution.reverseStr('abcdefg', 2)
