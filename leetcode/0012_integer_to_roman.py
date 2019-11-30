# -*- coding: utf-8 -*-

NUMERAL_ROMAN_MAP = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
]


class Solution:
    def intToRoman(self, num):
        result = []

        for numeral, roman in NUMERAL_ROMAN_MAP:
            while num >= numeral:
                result.append(roman)
                num -= numeral

        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()

    assert 'III' == solution.intToRoman(3)
    assert 'IV' == solution.intToRoman(4)
    assert 'IX' == solution.intToRoman(9)
    assert 'LVIII' == solution.intToRoman(58)
    assert 'MCMXCIV' == solution.intToRoman(1994)
