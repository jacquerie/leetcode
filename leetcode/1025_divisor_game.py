# -*- coding: utf-8 -*-


class Solution:
    def divisorGame(self, N):
        result = [False] * (N + 1)

        for i in range(2, N + 1):
            for j in range(1, i):
                if i % j == 0 and not result[i - j]:
                    result[i] = True

        return result[N]


if __name__ == '__main__':
    solution = Solution()

    assert solution.divisorGame(2)
    assert not solution.divisorGame(3)
