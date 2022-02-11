# -*- coding: utf-8 -*-


class Solution:
    def transformArray(self, arr):
        modified = True
        current = arr[:]
        while modified:
            modified = False
            previous = current[:]
            for i in range(1, len(previous) - 1):
                if previous[i - 1] < previous[i] and previous[i + 1] < previous[i]:
                    modified = True
                    current[i] -= 1
                elif previous[i - 1] > previous[i] and previous[i + 1] > previous[i]:
                    modified = True
                    current[i] += 1

        return current


if __name__ == "__main__":
    solution = Solution()

    assert [6, 3, 3, 4] == solution.transformArray([6, 2, 3, 4])
    assert [1, 4, 4, 4, 4, 5] == solution.transformArray([1, 6, 3, 4, 3, 5])
    assert [2, 2, 1, 1, 1, 2, 2, 1] == solution.transformArray([2, 1, 2, 1, 1, 2, 2, 1])
