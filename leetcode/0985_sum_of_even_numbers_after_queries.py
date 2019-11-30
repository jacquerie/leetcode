# -*- coding: utf-8 -*-


class Solution:
    def sumEvenAfterQueries(self, A, queries):
        result = []

        sumEven = 0
        for el in A:
            if el % 2 == 0:
                sumEven += el

        for val, index in queries:
            A[index] += val
            if A[index] % 2 == 0 and val % 2 == 0:
                sumEven += val
            elif A[index] % 2 == 0 and val % 2 == 1:
                sumEven += A[index]
            elif A[index] % 2 == 1 and val % 2 == 1:
                sumEven -= A[index] - val
            result.append(sumEven)

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [8, 6, 2, 4] == solution.sumEvenAfterQueries(
        [1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]])
