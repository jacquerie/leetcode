# -*- coding: utf-8 -*-

import itertools


class Solution:
    SQUARES = {i * i for i in range(1, 251)}

    def countTriples(self, n: int) -> int:
        result = 0
        for a, b in itertools.product(range(1, n + 1), repeat=2):
            sum_of_squares = a * a + b * b
            if sum_of_squares in self.SQUARES and sum_of_squares <= n * n:
                result += 1
        return result


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.countTriples(5)
    assert 4 == solution.countTriples(10)
    assert 4 == solution.countTriples(12)
