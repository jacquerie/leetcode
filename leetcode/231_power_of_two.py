# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def isPowerOfTwo(self, n):
        return (
            n == 1 or
            n == 2 or
            n == 4 or
            n == 8 or
            n == 16 or
            n == 32 or
            n == 64 or
            n == 128 or
            n == 256 or
            n == 512 or
            n == 1024 or
            n == 2048 or
            n == 4096 or
            n == 8192 or
            n == 16384 or
            n == 32768 or
            n == 65536 or
            n == 131072 or
            n == 262144 or
            n == 524288 or
            n == 1048576 or
            n == 2097152 or
            n == 4194304 or
            n == 8388608 or
            n == 16777216 or
            n == 33554432 or
            n == 67108864 or
            n == 134217728 or
            n == 268435456 or
            n == 536870912 or
            n == 1073741824
        )


if __name__ == '__main__':
    solution = Solution()

    assert solution.isPowerOfTwo(1)
    assert solution.isPowerOfTwo(16)
    assert not solution.isPowerOfTwo(218)
