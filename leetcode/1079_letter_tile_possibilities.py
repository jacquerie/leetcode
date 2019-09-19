# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools


class Solution(object):
    def numTilePossibilities(self, tiles):
        return sum(len(set(itertools.permutations(tiles, i))) for i in xrange(1, len(tiles) + 1))


if __name__ == '__main__':
    solution = Solution()

    assert 8 == solution.numTilePossibilities('AAB')
    assert 188 == solution.numTilePossibilities('AAABBC')
