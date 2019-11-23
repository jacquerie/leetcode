# -*- coding: utf-8 -*-


class Solution(object):
    def checkPossibility(self, nums):
        peak = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if peak is not None:
                    return False
                peak = i

        return (
            peak is None or
            peak == 0 or
            peak == len(nums) - 2 or
            nums[peak - 1] <= nums[peak + 1] or
            nums[peak] <= nums[peak + 2]
        )


if __name__ == '__main__':
    solution = Solution()

    assert solution.checkPossibility([4, 2, 3])
    assert not solution.checkPossibility([4, 2, 1])
    assert solution.checkPossibility([1, 2, 4, 5, 3])
    assert solution.checkPossibility([1, 1, 1])
    assert not solution.checkPossibility([3, 4, 2, 3])
