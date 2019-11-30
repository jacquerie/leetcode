# -*- coding: utf-8 -*-


class Solution:
    def sortedSquares(self, A):
        result = []

        i, j = 0, len(A) - 1
        while i <= j:
            if abs(A[i]) < abs(A[j]):
                result.append(A[j] * A[j])
                j -= 1
            else:
                result.append(A[i] * A[i])
                i += 1

        return result[::-1]


if __name__ == '__main__':
    solution = Solution()

    assert [0, 1, 9, 16, 100] == solution.sortedSquares([-4, -1, 0, 3, 10])
    assert [4, 9, 9, 49, 121] == solution.sortedSquares([-7, -3, 2, 3, 11])
