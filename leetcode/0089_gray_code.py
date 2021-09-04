# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            result.extend([el + 2 ** i for el in reversed(result)])
        return result


if __name__ == '__main__':
    solution = Solution()

    assert [0, 1, 3, 2] == solution.grayCode(2)
    assert [0, 1] == solution.grayCode(1)
