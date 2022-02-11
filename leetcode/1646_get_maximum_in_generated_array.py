# -*- coding: utf-8 -*-


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums, result = [0] * (n + 1), 0
        for i in range(1, n + 1):
            if i == 1:
                nums[i] = 1
            elif i % 2 == 0:
                nums[i] = nums[i // 2]
            elif i % 2 == 1:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
            result = max(result, nums[i])
        return result


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.getMaximumGenerated(7)
    assert 1 == solution.getMaximumGenerated(2)
    assert 2 == solution.getMaximumGenerated(3)
