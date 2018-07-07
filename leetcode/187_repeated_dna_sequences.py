# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools
from collections import Counter


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        counter = Counter(self.eachCons(s, n=10))
        return [''.join(k) for k, v in counter.iteritems() if v > 1]

    def eachCons(self, xs, n=10):
        return itertools.izip(*(xs[i:] for i in xrange(n)))


if __name__ == '__main__':
    solution = Solution()

    expected = ['AAAAACCCCC', 'CCCCCAAAAA']
    result = solution.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')

    assert sorted(expected) == sorted(result)
