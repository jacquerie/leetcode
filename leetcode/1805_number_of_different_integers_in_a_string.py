# -*- coding: utf-8 -*-

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        result = set()

        number = None
        for char in word:
            if char.isdigit() and number is None:
                number = int(char)
            elif char.isdigit() and number is not None:
                number = 10 * number + int(char)
            elif number is not None:
                result.add(number)
                number = None
        if number is not None:
            result.add(number)
            number = None

        return len(result)


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.numDifferentIntegers('a123bc34d8ef34')
    assert 2 == solution.numDifferentIntegers('leet1234code234')
    assert 1 == solution.numDifferentIntegers('a1b01c001')
