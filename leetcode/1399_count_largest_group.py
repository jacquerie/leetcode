# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = Counter()
        for i in range(1, n + 1):
            groups[self.sumOfDigits(i)] += 1
        return list(groups.values()).count(max(groups.values()))

    def sumOfDigits(self, n: int) -> int:
        return sum(int(digit) for digit in str(n))


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.countLargestGroup(13)
    assert 2 == solution.countLargestGroup(2)
    assert 6 == solution.countLargestGroup(15)
    assert 5 == solution.countLargestGroup(24)
