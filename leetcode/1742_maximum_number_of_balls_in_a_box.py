# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = Counter()
        for i in range(lowLimit, highLimit + 1):
            boxes[self.sumOfDigits(i)] += 1
        return max(boxes.values())

    def sumOfDigits(self, n: int) -> int:
        return sum(int(digit) for digit in str(n))


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.countBalls(1, 10)
    assert 2 == solution.countBalls(5, 15)
    assert 2 == solution.countBalls(19, 28)
