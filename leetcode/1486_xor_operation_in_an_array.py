# -*- coding: utf-8 -*-

import functools
import operator


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return functools.reduce(operator.xor, (start + 2 * i for i in range(n)))


if __name__ == '__main__':
    solution = Solution()

    assert 8 == solution.xorOperation(5, 0)
    assert 8 == solution.xorOperation(4, 3)
    assert 7 == solution.xorOperation(1, 7)
    assert 2 == solution.xorOperation(10, 5)
