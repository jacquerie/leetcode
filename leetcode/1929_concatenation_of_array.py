# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


if __name__ == '__main__':
    solution = Solution()

    assert [1, 2, 1, 1, 2, 1] == solution.getConcatenation([1, 2, 1])
    assert [1, 3, 2, 1, 1, 3, 2, 1] == solution.getConcatenation([1, 3, 2, 1])
