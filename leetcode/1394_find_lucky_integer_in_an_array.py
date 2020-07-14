# -*- coding: utf-8 -*-

from collections import Counter
from operator import itemgetter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for el, count in sorted(Counter(arr).items(), key=itemgetter(1), reverse=True):
            if el == count:
                return el
        return -1


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.findLucky([2, 2, 3, 4])
    assert 3 == solution.findLucky([1, 2, 2, 3, 3, 3])
    assert -1 == solution.findLucky([2, 2, 2, 3, 3])
    assert -1 == solution.findLucky([5])
    assert 7 == solution.findLucky([7, 7, 7, 7, 7, 7, 7])
