# -*- coding: utf-8 -*-


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        occurrences = {}
        for i, num in enumerate(nums):
            if num in occurrences and abs(i - occurrences[num]) <= k:
                return True
            occurrences[num] = i

        return False


if __name__ == '__main__':
    solution = Solution()

    assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3)
    assert solution.containsNearbyDuplicate([1, 0, 1, 1], 1)
    assert not solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
