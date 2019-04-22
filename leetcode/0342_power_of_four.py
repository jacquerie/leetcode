# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def isPowerOfFour(self, num):
        return (
            num == 1 or
            num == 4 or
            num == 16 or
            num == 64 or
            num == 256 or
            num == 1024 or
            num == 4096 or
            num == 16384 or
            num == 65536 or
            num == 262144 or
            num == 1048576 or
            num == 4194304 or
            num == 16777216 or
            num == 67108864 or
            num == 268435456 or
            num == 1073741824
        )


if __name__ == '__main__':
    solution = Solution()

    assert solution.isPowerOfFour(16)
    assert not solution.isPowerOfFour(5)
