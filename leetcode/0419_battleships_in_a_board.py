# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def countBattleships(self, board):
        result = 0
        if not board or not board[0]:
            return result

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                result += 1 if (
                    (i == 0 or board[i - 1][j] != 'X') and
                    (j == 0 or board[i][j - 1] != 'X') and
                    board[i][j] == 'X'
                ) else 0

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.countBattleships([
        ['X', '.', '.', 'X'],
        ['.', '.', '.', 'X'],
        ['.', '.', '.', 'X'],
    ])
