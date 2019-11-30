# -*- coding: utf-8 -*-


class Solution:
    def detectCapitalUse(self, word):
        if all(char.isupper() for char in word):
            return True
        elif all(char.islower() for char in word):
            return True
        elif word[0].isupper() and all(char.islower() for char in word[1:]):
            return True
        return False


if __name__ == '__main__':
    solution = Solution()

    assert solution.detectCapitalUse('USA')
    assert solution.detectCapitalUse('leetcode')
    assert solution.detectCapitalUse('Google')
    assert not solution.detectCapitalUse('FlaG')
