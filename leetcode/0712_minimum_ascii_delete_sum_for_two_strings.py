# -*- coding: utf-8 -*-


class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        result = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    result[i][j] = 0
                elif i == 0:
                    result[i][j] = sum(ord(c) for c in s2[:j])
                elif j == 0:
                    result[i][j] = sum(ord(c) for c in s1[:i])
                else:
                    if s1[i - 1] == s2[j - 1]:
                        result[i][j] = result[i - 1][j - 1]
                    else:
                        result[i][j] = min(
                            result[i - 1][j] + ord(s1[i - 1]),
                            result[i][j - 1] + ord(s2[j - 1]),
                        )

        return result[len(s1)][len(s2)]


if __name__ == '__main__':
    solution = Solution()

    assert 231 == solution.minimumDeleteSum('sea', 'eat')
    assert 403 == solution.minimumDeleteSum('delete', 'leet')
