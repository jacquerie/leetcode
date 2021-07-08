# -*- coding: utf-8 -*-

class Solution:
    def minOperations(self, n: int) -> int:
        return n * n // 4


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.minOperations(3)
    assert 9 == solution.minOperations(6)
