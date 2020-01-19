# -*- coding: utf-8 -*-


class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = list(str(num))
        for i, digit in enumerate(digits):
            if digit == '6':
                digits[i] = '9'
                break

        return int(''.join(digits))


if __name__ == '__main__':
    solution = Solution()

    assert 9969 == solution.maximum69Number(9669)
    assert 9999 == solution.maximum69Number(9996)
    assert 9999 == solution.maximum69Number(9999)
