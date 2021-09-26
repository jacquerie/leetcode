# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for length in range(1, len(arr) + 1, 2):
            for i in range(len(arr) - length + 1):
                result += sum(arr[i:i + length])
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 58 == solution.sumOddLengthSubarrays([1, 4, 2, 5, 3])
    assert 3 == solution.sumOddLengthSubarrays([1, 2])
    assert 66 == solution.sumOddLengthSubarrays([10, 11, 12])
