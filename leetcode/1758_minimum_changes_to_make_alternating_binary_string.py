# -*- coding: utf-8 -*-

class Solution:
    def minOperations(self, s: str) -> int:
        result = sum(index % 2 == int(char) for index, char in enumerate(s))
        return min(result, len(s) - result)


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.minOperations('0100')
    assert 0 == solution.minOperations('10')
    assert 2 == solution.minOperations('1111')
