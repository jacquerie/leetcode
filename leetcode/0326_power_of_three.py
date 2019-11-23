# -*- coding: utf-8 -*-


class Solution(object):
    def isPowerOfThree(self, n):
        return (
            n == 1 or
            n == 3 or
            n == 9 or
            n == 27 or
            n == 81 or
            n == 243 or
            n == 729 or
            n == 2187 or
            n == 6561 or
            n == 19683 or
            n == 59049 or
            n == 177147 or
            n == 531441 or
            n == 1594323 or
            n == 4782969 or
            n == 14348907 or
            n == 43046721 or
            n == 129140163 or
            n == 387420489 or
            n == 1162261467
        )


if __name__ == '__main__':
    solution = Solution()

    assert solution.isPowerOfThree(27)
