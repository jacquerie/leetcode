# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [] if n % 2 == 0 else [0]
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        return result


if __name__ == "__main__":
    solution = Solution()

    assert [0, 1, -1, 2, -2] == solution.sumZero(5)
    assert [0, 1, -1] == solution.sumZero(3)
    assert [0] == solution.sumZero(1)
