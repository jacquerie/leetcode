# -*- coding: utf-8 -*-

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for index, digit in enumerate(reversed(num)):
            if int(digit) % 2 == 1:
                return num[:len(num) - index]
        return ''


if __name__ == '__main__':
    solution = Solution()

    assert '5' == solution.largestOddNumber('52')
    assert '' == solution.largestOddNumber('4206')
    assert '35427' == solution.largestOddNumber('35427')
