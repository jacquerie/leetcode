# -*- coding: utf-8 -*-

import itertools


class Solution:
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
