# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    solution = Solution()

    assert solution.isAnagram('anagram', 'nagaram')
    assert solution.isAnagram('rat', 'car')
