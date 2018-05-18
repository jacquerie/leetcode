# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def isInvalidSubset(self, subset):
        return any(v > 1 and k != '.' for k, v in Counter(subset).items())

    def isValidSudoku(self, board):
        for i in range(9):
            if self.isInvalidSubset(board[i]):
                return False

        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            if self.isInvalidSubset(column):
                return False

        for i in range(3):
            for j in range(3):
                square = []
                for h in range(3):
                    for k in range(3):
                        square.append(board[3 * i + h][3 * j + k])
                if self.isInvalidSubset(square):
                    return False

        return True


if __name__ == '__main__':
    solution = Solution()

    assert solution.isValidSudoku([
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ])
    assert not solution.isValidSudoku([
        ['8', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ])
