# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def checkPerfectNumber(self, num):
        return (
            num == 6 or
            num == 28 or
            num == 496 or
            num == 8128 or
            num == 33550336
        )


if __name__ == '__main__':
    solution = Solution()

    assert solution.checkPerfectNumber(28)
