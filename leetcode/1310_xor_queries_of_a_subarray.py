# -*- coding: utf-8 -*-

from itertools import accumulate
from operator import xor
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xors = list(accumulate([0] + arr, xor))
        return [prefix_xors[j + 1] ^ prefix_xors[i] for i, j in queries]


if __name__ == '__main__':
    solution = Solution()

    assert [2, 7, 14, 8] == solution.xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]])
    assert [8, 0, 4, 4] == solution.xorQueries([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]])
