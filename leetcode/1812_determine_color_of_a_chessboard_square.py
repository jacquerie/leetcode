# -*- coding: utf-8 -*-

from typing import Tuple


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = self.coordinatesToCartesian(coordinates)
        return (x + y) % 2 == 1

    def coordinatesToCartesian(self, coordinates: str) -> Tuple[int, int]:
        column, row = coordinates
        return int(row) - 1, ord(column) - ord('a')


if __name__ == '__main__':
    solution = Solution()

    assert not solution.squareIsWhite('a1')
    assert solution.squareIsWhite('h3')
    assert not solution.squareIsWhite('c7')
