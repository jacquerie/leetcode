# -*- coding: utf-8 -*-


class Solution:
    def findMin(self, nums):
        first, last = 0, len(nums) - 1
        target = nums[-1]

        while first < last:
            mid = (first + last) // 2
            if nums[mid] <= target:
                last = mid
            else:
                first = mid + 1

        return nums[first]


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.findMin([3, 4, 5, 1, 2])
    assert 0 == solution.findMin([4, 5, 6, 7, 0, 1, 2])
    assert 1 == solution.findMin([2, 1])
    assert 1 == solution.findMin([3, 1, 2])
