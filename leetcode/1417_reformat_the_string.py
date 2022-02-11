# -*- coding: utf-8 -*-


class Solution:
    def reformat(self, s: str) -> str:
        digits, letters = [], []
        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                letters.append(char)

        if abs(len(digits) - len(letters)) > 1:
            return ""

        result = []

        more_digits_than_letters = len(digits) > len(letters)
        while digits or letters:
            char = digits.pop() if more_digits_than_letters else letters.pop()
            more_digits_than_letters = not more_digits_than_letters
            result.append(char)

        return "".join(reversed(result))


if __name__ == "__main__":
    solution = Solution()

    assert "0a1b2c" == solution.reformat("a0b1c2")
    assert "" == solution.reformat("leetcode")
    assert "" == solution.reformat("1229857369")
    assert "c2o0v1i9d" == solution.reformat("covid2019")
    assert "1a2b3" == solution.reformat("ab123")
