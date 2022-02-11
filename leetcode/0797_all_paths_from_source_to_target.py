# -*- coding: utf-8 -*-


class Solution:
    def bfs(self, graph, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in set(graph[vertex]) - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def allPathsSourceTarget(self, graph):
        return list(self.bfs(graph, 0, len(graph) - 1))


if __name__ == "__main__":
    solution = Solution()

    assert sorted([[0, 1, 3], [0, 2, 3]]) == sorted(
        solution.allPathsSourceTarget([[1, 2], [3], [3], []])
    )
