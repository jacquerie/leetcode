# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools


class Solution(object):
    def countLetters(self, S):
        result = 0

        for _, group in itertools.groupby(S):
            length = len(list(group))
            result += length * (length + 1) / 2

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 8 == solution.countLetters('aaaba')
    assert 55 == solution.countLetters('aaaaaaaaaa')
