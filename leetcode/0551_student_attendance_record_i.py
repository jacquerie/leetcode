# -*- coding: utf-8 -*-


class Solution(object):
    def checkRecord(self, s):
        return s.count('A') <= 1 and 'LLL' not in s


if __name__ == '__main__':
    solution = Solution()

    assert solution.checkRecord('PPALLP')
    assert not solution.checkRecord('PPALLL')
