# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[' ' for i in range(3)] for j in range(3)]
        for n, (x, y) in enumerate(moves, 1):
            board[x][y] = 'A' if n % 2 == 1 else 'B'
            winner = self.winner(board)
            if winner == 'A':
                return 'A'
            elif winner == 'B':
                return 'B'
            elif winner is None and n == 9:
                return 'Draw'
        return 'Pending'

    def winner(self, board: List[List[str]]) -> str:
        checks = [
            # Rows
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            # Cols
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            # Diags
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]],
        ]
        for check in checks:
            els = [board[x][y] for x, y in check]
            if els[0] != ' ' and len(set(els)) == 1:
                return els[0]


if __name__ == '__main__':
    solution = Solution()

    assert 'A' == solution.tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]])
    assert 'B' == solution.tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]])
    assert 'Draw' == solution.tictactoe([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]])
    assert 'Pending' == solution.tictactoe([[0, 0], [1, 1]])
