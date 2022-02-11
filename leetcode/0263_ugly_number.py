# -*- coding: utf-8 -*-


class Solution:
    def isUgly(self, num):
        if num == 0:
            return False

        for i in (2, 3, 5):
            while num % i == 0:
                num //= i

        return num == 1


if __name__ == "__main__":
    solution = Solution()

    assert solution.isUgly(1)
    assert solution.isUgly(6)
    assert solution.isUgly(8)
    assert not solution.isUgly(14)
    assert not solution.isUgly(0)
