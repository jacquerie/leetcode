# -*- coding: utf-8 -*-

import itertools


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zero_group_max_length, one_group_max_length = float('-inf'), float('-inf')
        for digit, group in itertools.groupby(s):
            if digit == '0':
                zero_group_max_length = max(zero_group_max_length, len(list(group)))
            elif digit == '1':
                one_group_max_length = max(one_group_max_length, len(list(group)))
        return zero_group_max_length < one_group_max_length


if __name__ == '__main__':
    solution = Solution()

    assert solution.checkZeroOnes('1101')
    assert not solution.checkZeroOnes('111000')
    assert not solution.checkZeroOnes('110100010')
