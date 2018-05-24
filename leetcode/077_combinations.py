# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools


class Solution(object):
    def combine(self, n, k):
        return [list(el) for el in itertools.combinations(range(1, n + 1), k)]


if __name__ == '__main__':
    solution = Solution()

    assert [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4],
    ] == solution.combine(4, 2)
