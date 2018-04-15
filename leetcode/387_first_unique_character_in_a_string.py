# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        counter = Counter(s)
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()

    assert 0 == solution.firstUniqChar('leetcode')
    assert 2 == solution.firstUniqChar('loveleetcode')
    assert -1 == solution.firstUniqChar('')
