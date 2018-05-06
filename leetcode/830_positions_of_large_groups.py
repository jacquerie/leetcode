# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools


class Solution(object):
    def largeGroupPositions(self, S):
        index = 0
        result = []

        for _, group in itertools.groupby(S):
            length = len(list(group))
            if length >= 3:
                result.append([index, index + length - 1])
            index += length

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [[3, 6]] == solution.largeGroupPositions('abbxxxxzzy')
    assert [] == solution.largeGroupPositions('abc')
    assert [[3,5],[6,9],[12,14]] == solution.largeGroupPositions('abcdddeeeeaabbbcd')
