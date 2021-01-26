# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for el in encoded:
            result.append(el ^ result[-1])
        return result


if __name__ == '__main__':
    solution = Solution()

    assert [1, 0, 2, 1] == solution.decode([1, 2, 3], 1)
    assert [4, 2, 0, 7, 4] == solution.decode([6, 2, 7, 3], 4)
