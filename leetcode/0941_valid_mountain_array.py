# -*- coding: utf-8 -*-


class Solution(object):
    def validMountainArray(self, A):
        if len(A) < 3:
            return False

        i, j = 0, len(A) - 1
        while i < len(A) - 1 and A[i] < A[i + 1]:
            i += 1
        while j > 0 and A[j] < A[j - 1]:
            j -= 1
        return 0 < i == j < len(A) - 1


if __name__ == '__main__':
    solution = Solution()

    assert not solution.validMountainArray([2, 1])
    assert not solution.validMountainArray([3, 5, 5])
    assert solution.validMountainArray([0, 3, 2, 1])
    assert not solution.validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
