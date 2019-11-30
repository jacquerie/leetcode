# -*- coding: utf-8 -*-


class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()

        min_abs_difference, result = float('inf'), []
        for i in range(len(arr) - 1):
            abs_difference = abs(arr[i + 1] - arr[i])
            if abs_difference < min_abs_difference:
                min_abs_difference = abs_difference
                result = [[arr[i], arr[i + 1]]]
            elif abs_difference == min_abs_difference:
                result.append([arr[i], arr[i + 1]])
        return result


if __name__ == '__main__':
    solution = Solution()

    assert [[1, 2], [2, 3], [3, 4]] == solution.minimumAbsDifference([4, 2, 1, 3])
    assert [[1, 3]] == solution.minimumAbsDifference([1, 3, 6, 10, 15])
    assert [[-14, -10], [19, 23], [23, 27]] == solution.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27])
