# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools


class Solution(object):
    def isAlienSorted(self, words, order):
        for i in xrange(len(words) - 1):
            if not self.isAlienLessOrEqual(words[i], words[i + 1], order):
                return False
        return True

    def isAlienLessOrEqual(self, word1, word2, order):
        rank = {c: i for i, c in enumerate(order)}
        for char1, char2 in itertools.izip_longest(word1, word2):
            if char1 is None:
                return True
            elif char2 is None:
                return False
            elif rank[char1] > rank[char2]:
                return False
            elif rank[char1] < rank[char2]:
                return True
        return True


if __name__ == '__main__':
    solution = Solution()

    assert solution.isAlienSorted(['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz')
    assert not solution.isAlienSorted(['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz')
    assert not solution.isAlienSorted(['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz')
