# -*- coding: utf-8 -*-

ROMAN_NUMERAL_MAP = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


class Solution:
    def romanToInt(self, s):
        result = 0

        for i, c in enumerate(s):
            if i > 0 and ROMAN_NUMERAL_MAP[c] > ROMAN_NUMERAL_MAP[s[i - 1]]:
                result += ROMAN_NUMERAL_MAP[c] - 2 * ROMAN_NUMERAL_MAP[s[i - 1]]
            else:
                result += ROMAN_NUMERAL_MAP[c]

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.romanToInt('III')
    assert 4 == solution.romanToInt('IV')
    assert 9 == solution.romanToInt('IX')
    assert 58 == solution.romanToInt('LVIII')
    assert 1994 == solution.romanToInt('MCMXCIV')
