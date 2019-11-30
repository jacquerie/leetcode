# -*- coding: utf-8 -*-


class Solution:
    def calculateMinimumHP(self, dungeon):
        result = [float('inf') for _ in range(len(dungeon[0]))]
        result[-1] = 1

        for i in reversed(range(len(dungeon))):
            result[-1] = max(result[-1] - dungeon[i][-1], 1)
            for j in reversed(range(len(dungeon[0]) - 1)):
                result[j] = max(min(result[j], result[j + 1]) - dungeon[i][j], 1)

        return result[0]


if __name__ == '__main__':
    solution = Solution()

    assert 7 == solution.calculateMinimumHP([
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5],
    ])
