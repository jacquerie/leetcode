# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts, ends = set(), set()
        for (start, end) in paths:
            starts.add(start)
            ends.add(end)
        return ends.difference(starts).pop()


if __name__ == '__main__':
    solution = Solution()

    assert 'Sao Paulo' == solution.destCity([['London', 'New York'], ['New York', 'Lima'], ['Lima', 'Sao Paulo']])
    assert 'A' == solution.destCity([['B', 'C'], ['D', 'B'], ['C', 'A']])
    assert 'Z' == solution.destCity([['A', 'Z']])
