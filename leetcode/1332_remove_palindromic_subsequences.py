# -*- coding: utf-8 -*-


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        elif s == s[::-1]:
            return 1
        return 2


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.removePalindromeSub('ababa')
    assert 2 == solution.removePalindromeSub('abb')
    assert 2 == solution.removePalindromeSub('baabb')
    assert 0 == solution.removePalindromeSub('')
