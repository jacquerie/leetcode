# -*- coding: utf-8 -*-


class Solution:
    def flipAndInvertImage(self, A):
        return [[1 - el for el in row[::-1]] for row in A]


if __name__ == "__main__":
    solution = Solution()

    assert [[1, 0, 0], [0, 1, 0], [1, 1, 1],] == solution.flipAndInvertImage(
        [
            [1, 1, 0],
            [1, 0, 1],
            [0, 0, 0],
        ]
    )
