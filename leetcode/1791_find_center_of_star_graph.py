# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.findCenter([[1, 2], [2, 3], [4, 2]])
    assert 1 == solution.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]])
