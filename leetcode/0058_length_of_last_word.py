# -*- coding: utf-8 -*-


class Solution:
    def lengthOfLastWord(self, s):
        j = len(s) - 1
        while j >= 0 and s[j] == ' ':
            j -= 1

        i = j
        while i >= 0 and s[i] != ' ':
            i -= 1

        return j - i


if __name__ == '__main__':
    solution = Solution()

    assert 5 == solution.lengthOfLastWord('Hello World')
    assert 1 == solution.lengthOfLastWord('a')
    assert 1 == solution.lengthOfLastWord('a ')
