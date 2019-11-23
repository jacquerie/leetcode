# -*- coding: utf-8 -*-


class Solution(object):
    def canJump(self, nums):
        last = 0
        for i, num in enumerate(nums):
            if i > last:
                break
            last = max(last, i + num)
        return last >= len(nums) - 1


if __name__ == '__main__':
    solution = Solution()

    assert solution.canJump([2, 3, 1, 1, 4])
    assert not solution.canJump([3, 2, 1, 0, 4])
