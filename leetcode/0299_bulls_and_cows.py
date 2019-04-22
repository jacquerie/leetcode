# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def getHint(self, secret, guess):
        bulls = [s == g for s, g in zip(secret, guess)]
        cows = (Counter(secret) & Counter(guess)).values()
        return '{0}A{1}B'.format(sum(bulls), sum(cows) - sum(bulls))


if __name__ == '__main__':
    solution = Solution()

    assert '1A3B' == solution.getHint('1807', '7810')
    assert '1A1B' == solution.getHint('1123', '0111')
