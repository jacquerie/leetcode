# -*- coding: utf-8 -*-


class Solution:
    def findMaxAverage(self, nums, k):
        current_sum = sum(nums[:k])
        current_max = current_sum
        for i, num in enumerate(nums[k:], k):
            current_sum += nums[i] - nums[i - k]
            current_max = max(current_max, current_sum)
        return current_max / float(k)


if __name__ == "__main__":
    solution = Solution()

    assert 12.75 == solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
