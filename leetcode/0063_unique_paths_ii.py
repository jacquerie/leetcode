# -*- coding: utf-8 -*-


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        result = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    result[i][j] = 0
                elif i == 0 and j == 0:
                    result[i][j] = 1
                elif i == 0:
                    result[i][j] = result[i][j - 1]
                elif j == 0:
                    result[i][j] = result[i - 1][j]
                else:
                    result[i][j] = result[i - 1][j] + result[i][j - 1]

        return result[-1][-1]


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ])
    assert 1 == solution.uniquePathsWithObstacles([
        [0],
        [0],
    ])
