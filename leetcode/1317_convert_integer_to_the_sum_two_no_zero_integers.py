# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if '0' not in '%d%d' % (i, n - i):
                return [i, n - i]


if __name__ == '__main__':
    solution = Solution()

    assert [1, 1] == solution.getNoZeroIntegers(2)
    assert [2, 9] == solution.getNoZeroIntegers(11)
    assert [1, 9999] == solution.getNoZeroIntegers(10000)
    assert [1, 68] == solution.getNoZeroIntegers(69)
    assert [11, 999] == solution.getNoZeroIntegers(1010)
