# -*- coding: utf-8 -*-

from collections import deque


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        nr, nc = len(image), len(image[0])
        result = [[image[i][j] for j in range(nc)] for i in range(nr)]

        queue = deque([(sr, sc)])
        while queue:
            r, c = queue.pop()
            result[r][c] = newColor
            if 0 < r and image[r][c] == image[r - 1][c] and result[r - 1][c] != newColor:
                queue.append((r - 1, c))
            if r < nr - 1 and image[r][c] == image[r + 1][c] and result[r + 1][c] != newColor:
                queue.append((r + 1, c))
            if 0 < c and image[r][c] == image[r][c - 1] and result[r][c - 1] != newColor:
                queue.append((r, c - 1))
            if c < nc - 1 and image[r][c] == image[r][c + 1] and result[r][c + 1] != newColor:
                queue.append((r, c + 1))

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ] == solution.floodFill([
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ], 1, 1, 2)
