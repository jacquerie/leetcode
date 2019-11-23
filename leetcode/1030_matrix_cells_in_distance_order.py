# -*- coding: utf-8 -*-

from collections import deque


class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        queue, result, visited = deque([(r0, c0)]), [], set()

        while queue:
            r, c = queue.popleft()
            if (r, c) in visited:
                continue

            result.append([r, c])
            visited.add((r, c))

            if 0 < r:
                queue.append((r - 1, c))
            if 0 < c:
                queue.append((r, c - 1))
            if r < R - 1:
                queue.append((r + 1, c))
            if c < C - 1:
                queue.append((r, c + 1))

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [[0, 0], [0, 1]] == solution.allCellsDistOrder(1, 2, 0, 0)
    assert [[0, 1], [0, 0], [1, 1], [1, 0]] == solution.allCellsDistOrder(2, 2, 0, 1)
