# -*- coding: utf-8 -*-


class Solution(object):
    def shiftingLetters(self, S, shifts):
        result = []

        current_shift = 0
        for shift in shifts:
            current_shift += shift
            current_shift %= 26

        for i, c in enumerate(S):
            result.append(self.shiftLetter(c, current_shift))
            current_shift -= shifts[i]
            current_shift %= 26

        return ''.join(result)

    def shiftLetter(self, c, shift):
        return chr(ord('a') + (ord(c) + shift - ord('a')) % 26)


if __name__ == '__main__':
    solution = Solution()

    assert 'rpl' == solution.shiftingLetters('abc', [3, 5, 9])
