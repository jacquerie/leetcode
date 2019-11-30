# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        return (
            other is not None and
            self.val == other.val and
            self.left == other.left and
            self.right == other.right
        )


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return

        mid = len(nums) // 2

        result = TreeNode(nums[mid])
        result.left = self.sortedArrayToBST(nums[:mid])
        result.right = self.sortedArrayToBST(nums[mid + 1:])

        return result


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(0)
    t0_1 = TreeNode(-3)
    t0_2 = TreeNode(9)
    t0_3 = TreeNode(-10)
    t0_4 = TreeNode(5)
    t0_2.left = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert t0_0 == solution.sortedArrayToBST([-10, -3, 0, 5, 9])
