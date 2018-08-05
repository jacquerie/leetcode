# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools


class Solution(object):
    def reverseStr(self, s, k):
        result = []

        for chunk in self.chunkStr(s, 2 * k):
            result.append(reversed(chunk[:k]))
            result.append(chunk[k:])

        return ''.join(self.flattenLst(result))

    def chunkStr(self, s, k):
        for i in xrange((len(s) // k) + 1):
            start, end = k * i, k * i + k
            yield s[start:end]

    def flattenLst(self, l):
        return itertools.chain.from_iterable(l)


if __name__ == '__main__':
    solution = Solution()

    assert 'bacdfeg' == solution.reverseStr('abcdefg', 2)
