# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import deque


class Color(object):
    BLACK = 0
    WHITE = 1


class Solution(object):
    def isBipartite(self, graph):
        color = {}
        for node in xrange(len(graph)):
            if node in color:
                continue
            stack = deque([node])
            color[node] = Color.BLACK
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if neighbor not in color:
                        stack.append(neighbor)
                        if color[current] == Color.BLACK:
                            color[neighbor] = Color.WHITE
                        elif color[current] == Color.WHITE:
                            color[neighbor] = Color.BLACK
                    elif color[current] == color[neighbor]:
                        return False
        return True


if __name__ == '__main__':
    solution = Solution()

    assert solution.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]])
    assert not solution.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
    assert not solution.isBipartite([
        [],
        [2, 4, 6],
        [1, 4, 8, 9],
        [7, 8],
        [1, 2, 8, 9],
        [6, 9],
        [1, 5, 7, 8, 9],
        [3, 6, 9],
        [2, 3, 4, 6, 9],
        [2, 4, 5, 6, 7, 8],
    ])
