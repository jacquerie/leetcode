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
    def subtreeWithAllDeepest(self, root):
        _, result = self._subtreeWithAllDeepest(root)
        return result

    def _subtreeWithAllDeepest(self, root):
        if root is None:
            return 0, None

        leftDepth, leftResult = self._subtreeWithAllDeepest(root.left)
        rightDepth, rightResult = self._subtreeWithAllDeepest(root.right)

        if leftDepth > rightDepth:
            return 1 + leftDepth, leftResult
        elif leftDepth < rightDepth:
            return 1 + rightDepth, rightResult
        return 1 + rightDepth, root


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(3)
    t0_1 = TreeNode(5)
    t0_2 = TreeNode(1)
    t0_3 = TreeNode(6)
    t0_4 = TreeNode(2)
    t0_5 = TreeNode(0)
    t0_6 = TreeNode(8)
    t0_7 = TreeNode(7)
    t0_8 = TreeNode(4)
    t0_4.right = t0_8
    t0_4.left = t0_7
    t0_2.right = t0_6
    t0_2.left = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert t0_4 == solution.subtreeWithAllDeepest(t0_0)
