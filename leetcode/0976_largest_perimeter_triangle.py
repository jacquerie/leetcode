# -*- coding: utf-8 -*-


class Solution:
    def largestPerimeter(self, A):
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            if A[i + 2] + A[i + 1] > A[i]:
                return A[i + 2] + A[i + 1] + A[i]
        return 0


if __name__ == '__main__':
    solution = Solution()

    assert 5 == solution.largestPerimeter([2, 1, 2])
    assert 0 == solution.largestPerimeter([1, 2, 1])
    assert 10 == solution.largestPerimeter([3, 2, 3, 4])
    assert 8 == solution.largestPerimeter([3, 6, 2, 3])
