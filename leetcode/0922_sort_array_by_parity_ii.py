# -*- coding: utf-8 -*-


class Solution(object):
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]

        return A


if __name__ == '__main__':
    solution = Solution()

    assert [4, 5, 2, 7] == solution.sortArrayByParityII([4, 2, 5, 7])
