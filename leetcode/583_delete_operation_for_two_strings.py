# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def minDistance(self, word1, word2):
        result = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 and j == 0:
                    result[i][j] = 0
                elif i == 0:
                    result[i][j] = j
                elif j == 0:
                    result[i][j] = i
                else:
                    if word1[i - 1] == word2[j - 1]:
                        result[i][j] = result[i - 1][j - 1]
                    else:
                        result[i][j] = 1 + min(result[i - 1][j], result[i][j - 1])

        return result[len(word1)][len(word2)]


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.minDistance('sea', 'eat')
