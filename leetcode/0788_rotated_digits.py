# -*- coding: utf-8 -*-


class Solution(object):
    def rotateDigit(self, d):
        if d == '0':
            return '0'
        elif d == '1':
            return '1'
        elif d == '2':
            return '5'
        elif d == '5':
            return '2'
        elif d == '6':
            return '9'
        elif d == '8':
            return '8'
        elif d == '9':
            return '6'

    def rotatedDigits(self, N):
        result = 0

        for i in range(1, N + 1):
            rotated_digits = [self.rotateDigit(digit) for digit in list(str(i))]
            if None in rotated_digits:
                continue
            elif int(''.join(rotated_digits)) != i:
                result += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.rotatedDigits(10)
    assert 247 == solution.rotatedDigits(857)
