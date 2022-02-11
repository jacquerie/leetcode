# -*- coding: utf-8 -*-


class Solution:
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 == 0:
                i += 1
            elif A[j] % 2 == 1:
                j -= 1
            elif A[i] % 2 == 1 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1

        return A


if __name__ == "__main__":
    solution = Solution()

    assert [4, 2, 1, 3] == solution.sortArrayByParity([3, 1, 2, 4])
