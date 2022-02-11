# -*- coding: utf-8 -*-


class Solution:
    def solveSudoku(self, board):
        self.solveSudokuHelper(board)

    def solveSudokuHelper(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        board[i][j] = k
                        if self.isValidSudoku(board, i, j) and self.solveSudokuHelper(
                            board
                        ):
                            return True
                        board[i][j] = "."
                    return False
        return True

    def isValidSudoku(self, board, x, y):
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False

        for j in range(9):
            if j != y and board[x][j] == board[x][y]:
                return False

        for i in range(3):
            for j in range(3):
                if (
                    i != x % 3
                    and j != y % 3
                    and board[3 * (x // 3) + i][3 * (y // 3) + j] == board[x][y]
                ):
                    return False

        return True


if __name__ == "__main__":
    solution = Solution()

    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    solution.solveSudoku(board)

    assert [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ] == board
