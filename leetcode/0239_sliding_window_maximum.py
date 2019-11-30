# -*- coding: utf-8 -*-

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        seen = deque()

        for i, num in enumerate(nums):
            while seen and num >= nums[seen[-1]]:
                seen.pop()
            seen.append(i)
            if i >= k and seen and seen[0] == i - k:
                seen.popleft()
            if i >= k - 1:
                result.append(nums[seen[0]])

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [3, 3, 5, 5, 6, 7] == solution.maxSlidingWindow([
        1, 3, -1, -3, 5, 3, 6, 7], 3)
