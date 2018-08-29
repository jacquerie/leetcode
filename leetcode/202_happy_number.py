# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1:
            n = sum(int(char) ** 2 for char in str(n))
            if n in seen:
                return False
            seen.add(n)

        return True


if __name__ == '__main__':
    solution = Solution()

    assert solution.isHappy(19)
    assert not solution.isHappy(2)
