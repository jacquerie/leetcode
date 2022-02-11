# -*- coding: utf-8 -*-


class Solution:
    def exist(self, board, word):
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.startsHere(board, word, visited, 0, i, j):
                    return True
        return False

    def startsHere(self, board, word, visited, current, i, j):
        if current == len(word):
            return True

        out_of_bounds = i < 0 or i >= len(board) or j < 0 or j >= len(board[0])
        if out_of_bounds:
            return False

        already_visited = (i, j) in visited
        wrong_current_letter = board[i][j] != word[current]
        if already_visited or wrong_current_letter:
            return False

        visited.add((i, j))
        result = (
            self.startsHere(board, word, visited, current + 1, i - 1, j)
            or self.startsHere(board, word, visited, current + 1, i, j - 1)
            or self.startsHere(board, word, visited, current + 1, i + 1, j)
            or self.startsHere(board, word, visited, current + 1, i, j + 1)
        )
        visited.remove((i, j))

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.exist(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ],
        "ABCCED",
    )
    assert solution.exist(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ],
        "SEE",
    )
    assert not solution.exist(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ],
        "ABCB",
    )
