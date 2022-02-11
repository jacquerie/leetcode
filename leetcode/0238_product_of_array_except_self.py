# -*- coding: utf-8 -*-


class Solution:
    def productExceptSelf(self, nums):
        result = [1] * len(nums)

        previous = 1
        for i in range(len(nums) - 1):
            result[i + 1] = previous * nums[i]
            previous *= nums[i]

        previous = 1
        for i in range(len(nums) - 1, 0, -1):
            result[i - 1] *= previous * nums[i]
            previous *= nums[i]

        return result


if __name__ == "__main__":
    solution = Solution()

    assert [24, 12, 8, 6] == solution.productExceptSelf([1, 2, 3, 4])
