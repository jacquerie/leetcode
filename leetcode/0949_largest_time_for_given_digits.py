# -*- coding: utf-8 -*-

import itertools


class Solution(object):
    def largestTimeFromDigits(self, A):
        for digits in itertools.permutations(sorted(A, reverse=True)):
            if self.isValidTime(digits):
                return '{}{}:{}{}'.format(*digits)
        return ''

    def isValidTime(self, digits):
        hour = 10 * digits[0] + digits[1]
        minute = 10 * digits[2] + digits[3]
        return 0 <= hour <= 23 and 0 <= minute <= 59


if __name__ == '__main__':
    solution = Solution()

    assert '23:41' == solution.largestTimeFromDigits([1, 2, 3, 4])
    assert '' == solution.largestTimeFromDigits([5, 5, 5, 5])
    assert '00:00' == solution.largestTimeFromDigits([0, 0, 0, 0])
    assert '10:00' == solution.largestTimeFromDigits([0, 0, 1, 0])
