# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import deque


class Solution(object):
    def findCircleNum(self, M):
        result = 0

        for i in xrange(len(M)):
            if M[i][i]:
                result += 1
                self.markCircleAsVisited(M, i)

        return result

    def markCircleAsVisited(self, M, i):
        queue = deque([i])
        while queue:
            j = queue.pop()
            M[j][j] = 0
            for h, k in enumerate(M[j]):
                if k and M[h][h]:
                    queue.append(h)


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.findCircleNum([
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1],
    ])
    assert 1 == solution.findCircleNum([
        [1, 1, 0],
        [1, 1, 1],
        [0, 1, 1],
    ])
