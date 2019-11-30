# -*- coding: utf-8 -*-

from itertools import product

DIGIT_LETTERS_MAP = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        return [''.join(el) for el in product(*(DIGIT_LETTERS_MAP[digit] for digit in digits))]


if __name__ == '__main__':
    solution = Solution()

    assert ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'] == solution.letterCombinations('23')
