# -*- coding: utf-8 -*-


class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        digits = []
        while x:
            digits.append(x % 10)
            x //= 10

        return digits == digits[::-1]


if __name__ == "__main__":
    solution = Solution()

    assert solution.isPalindrome(121)
    assert not solution.isPalindrome(-121)
    assert not solution.isPalindrome(10)
