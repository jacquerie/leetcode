# -*- coding: utf-8 -*-

class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(str(num), reverse=True)
        return int(digits[0]) + int(digits[1]) + 10 * int(digits[2]) + 10 * int(digits[3])


if __name__ == '__main__':
    solution = Solution()

    assert 52 == solution.minimumSum(2932)
    assert 13 == solution.minimumSum(4009)
