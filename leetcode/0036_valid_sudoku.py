# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def isValidSudoku(self, board):
        for i in xrange(9):
            if self.isInvalidSubset(board[i][j] for j in xrange(9)):
                return False

        for j in xrange(9):
            if self.isInvalidSubset(board[i][j] for i in xrange(9)):
                return False

        for i in xrange(3):
            for j in xrange(3):
                if self.isInvalidSubset(board[3 * i + h][3 * j + k] for h in xrange(3) for k in xrange(3)):
                    return False

        return True

    def isInvalidSubset(self, subset):
        filtered_subset = [el for el in subset if el != '.']
        return len(set(filtered_subset)) != len(filtered_subset)


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
