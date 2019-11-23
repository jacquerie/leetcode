# -*- coding: utf-8 -*-


class Solution(object):
    def plusOne(self, digits):
        number = int(''.join(str(digit) for digit in digits))
        return [int(digit) for digit in str(number + 1)]


if __name__ == '__main__':
    solution = Solution()

    assert [1, 2, 4] == solution.plusOne([1, 2, 3])
    assert [4, 3, 2, 2] == solution.plusOne([4, 3, 2, 1])
