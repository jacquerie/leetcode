# -*- coding: utf-8 -*-


class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.containsDuplicate([1, 2, 3, 1])
    assert not solution.containsDuplicate([1, 2, 3, 4])
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
