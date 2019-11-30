# -*- coding: utf-8 -*-


class Solution:
    def matrixReshape(self, nums, r, c):
        original_r, original_c = len(nums), len(nums[0])
        if r * c != original_r * original_c:
            return nums

        tmp = [nums[i][j] for i in range(original_r) for j in range(original_c)]

        result = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(tmp[i * c + j])
            result.append(row)
        return result


if __name__ == '__main__':
    solution = Solution()

    assert [[1, 2, 3, 4]] == solution.matrixReshape([[1, 2], [3, 4]], 1, 4)
    assert [[1, 2], [3, 4]] == solution.matrixReshape([[1, 2], [3, 4]], 2, 4)
