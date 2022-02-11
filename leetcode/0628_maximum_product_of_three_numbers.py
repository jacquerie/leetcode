# -*- coding: utf-8 -*-


class Solution:
    def maximumProduct(self, nums):
        min1, min2 = float("inf"), float("inf")
        max1, max2, max3 = float("-inf"), float("-inf"), float("-inf")

        for num in nums:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num

            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num >= max3:
                max3 = num

        return max(max1 * max2 * max3, max1 * min1 * min2)


if __name__ == "__main__":
    solution = Solution()

    assert 6 == solution.maximumProduct([1, 2, 3])
    assert 24 == solution.maximumProduct([1, 2, 3, 4])
    assert 0 == solution.maximumProduct([0, 0, 0])
    assert -6 == solution.maximumProduct([-1, -2, -3])
