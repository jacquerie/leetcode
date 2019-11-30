# -*- coding: utf-8 -*-


class Solution:
    def prisonAfterNDays(self, cells, N):
        for i in range(N % 14 + 14):
            cells = tuple(
                1 if 0 < j < 7 and cells[j - 1] == cells[j + 1] else 0 for j in range(8))
        return list(cells)


if __name__ == '__main__':
    solution = Solution()

    assert [0, 0, 1, 1, 0, 0, 0, 0] == solution.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7)
    assert [0, 0, 1, 1, 1, 1, 1, 0] == solution.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000)
    assert [0, 0, 1, 0, 0, 1, 0, 0] == solution.prisonAfterNDays([1, 1, 0, 1, 1, 0, 1, 1], 6)
    assert [0, 0, 0, 1, 1, 0, 1, 0] == solution.prisonAfterNDays([0, 0, 0, 1, 1, 0, 1, 0], 574)
    assert [0, 1, 1, 0, 1, 1, 1, 0] == solution.prisonAfterNDays([1, 0, 0, 1, 0, 0, 0, 1], 826)
