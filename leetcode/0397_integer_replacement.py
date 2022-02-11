# -*- coding: utf-8 -*-


class Solution:
    def integerReplacement(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        elif n % 4 == 1:
            return 3 + self.integerReplacement((n - 1) // 4)
        elif n % 4 == 3:
            return 3 + self.integerReplacement((n + 1) // 4)
        return 1 + self.integerReplacement(n // 2)


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.integerReplacement(8)
    assert 4 == solution.integerReplacement(7)
