# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        return self._hasPathSum(root, sum)

    def _hasPathSum(self, root, sum):
        if root.left is None and root.right is None:
            return sum == root.val
        elif root.left is None:
            return self._hasPathSum(root.right, sum - root.val)
        elif root.right is None:
            return self._hasPathSum(root.left, sum - root.val)
        return self._hasPathSum(root.left, sum - root.val) or self._hasPathSum(
            root.right, sum - root.val
        )


if __name__ == "__main__":
    solution = Solution()

    t0_0 = TreeNode(5)
    t0_1 = TreeNode(4)
    t0_2 = TreeNode(8)
    t0_3 = TreeNode(11)
    t0_4 = TreeNode(13)
    t0_5 = TreeNode(4)
    t0_6 = TreeNode(7)
    t0_7 = TreeNode(2)
    t0_8 = TreeNode(1)
    t0_5.right = t0_8
    t0_3.right = t0_7
    t0_3.left = t0_6
    t0_2.right = t0_5
    t0_2.left = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert solution.hasPathSum(t0_0, 22)
