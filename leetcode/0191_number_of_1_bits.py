# -*- coding: utf-8 -*-


class Solution:
    def hammingWeight(self, n):
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.hammingWeight(11)
    assert 1 == solution.hammingWeight(128)
