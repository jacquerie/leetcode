# -*- coding: utf-8 -*-

from collections import deque


class Color:
    BLACK = 0
    WHITE = 1


class Solution:
    def possibleBipartition(self, N, dislikes):
        return self.isBipartite(self.toGraph(range(N), dislikes))

    def toGraph(self, vertices, edges):
        result = [[] for vertex in vertices]
        for i, j in edges:
            result[i - 1].append(j - 1)
            result[j - 1].append(i - 1)
        return result

    def isBipartite(self, graph):
        color = {}
        for node in range(len(graph)):
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

    assert solution.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]])
    assert not solution.possibleBipartition(3, [[1, 2], [1, 3], [2, 3]])
    assert not solution.possibleBipartition(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]])
