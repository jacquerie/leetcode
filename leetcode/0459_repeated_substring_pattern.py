# -*- coding: utf-8 -*-


class Solution:
    def repeatedSubstringPattern(self, s):
        length = len(s)
        for i in range(1, length // 2 + 1):
            if length % i == 0 and s[:i] * (length // i) == s:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()

    assert solution.repeatedSubstringPattern('abab')
    assert not solution.repeatedSubstringPattern('aba')
    assert solution.repeatedSubstringPattern('abcabcabcabc')
