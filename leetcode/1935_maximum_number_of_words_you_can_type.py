# -*- coding: utf-8 -*-

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result = 0

        seen_broken_letter = False
        for char in text:
            if char.isspace():
                seen_broken_letter, result = False, result + (1 if not seen_broken_letter else 0)
            elif char in brokenLetters:
                seen_broken_letter = True
        seen_broken_letter, result = False, result + (1 if not seen_broken_letter else 0)

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.canBeTypedWords('hello world', 'ad')
    assert 1 == solution.canBeTypedWords('leet code', 'lt')
    assert 0 == solution.canBeTypedWords('leet code', 'e')
