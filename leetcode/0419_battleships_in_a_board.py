# -*- coding: utf-8 -*-


class Solution:
    def countBattleships(self, board):
        result = 0
        if not board or not board[0]:
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
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
