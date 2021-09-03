# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join(str(1 - int(num[i])) for i, num in enumerate(nums))


if __name__ == '__main__':
    solution = Solution()

    assert '11' == solution.findDifferentBinaryString(['01', '10'])
    assert '10' == solution.findDifferentBinaryString(['00', '01'])
    assert '000' == solution.findDifferentBinaryString(['111', '011', '001'])
