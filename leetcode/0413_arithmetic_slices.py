# -*- coding: utf-8 -*-


class Solution:
    def numberOfArithmeticSlices(self, A):
        result = 0
        if len(A) < 3:
            return result

        first, step = 0, A[1] - A[0]
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == step:
                result += i - first - 1
            else:
                first, step = i - 1, A[i] - A[i - 1]

        return result


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.numberOfArithmeticSlices([1, 2, 3, 4])
    assert 2 == solution.numberOfArithmeticSlices([1, 2, 3, 5, 8, 9, 10])
