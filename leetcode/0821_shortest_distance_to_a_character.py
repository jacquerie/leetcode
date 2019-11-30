# -*- coding: utf-8 -*-


class Solution:
    def shortestToChar(self, S, C):
        result = []

        indices = [i for i, c in enumerate(S) if c == C]
        for i in range(len(S)):
            result.append(min(abs(i - j) for j in indices))

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0] == solution.shortestToChar('loveleetcode', 'e')
