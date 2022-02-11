# -*- coding: utf-8 -*-


class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.computeSquare(board, i, j)
        for i in range(m):
            for j in range(n):
                self.updateSquare(board, i, j)

    def computeSquare(self, board, i, j):
        alive, dead = board[i][j], not board[i][j]
        live_neighbors = self.countLiveNeighbors(board, i, j)
        if alive and 2 <= live_neighbors <= 3:
            board[i][j] |= 2
        elif dead and live_neighbors == 3:
            board[i][j] |= 2

    def countLiveNeighbors(self, board, i, j):
        return sum(el & 1 for el in self.getNeighbors(board, i, j))

    def getNeighbors(self, board, i, j):
        m, n = len(board), len(board[0])
        for h in (-1, 0, 1):
            for k in (-1, 0, 1):
                if not (h == 0 and k == 0):
                    if 0 <= i + h < m and 0 <= j + k < n:
                        yield board[i + h][j + k]

    def updateSquare(self, board, i, j):
        board[i][j] >>= 1


if __name__ == "__main__":
    solution = Solution()

    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0],
    ]

    assert solution.gameOfLife(board) is None
    assert [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 1, 0],
    ] == board
