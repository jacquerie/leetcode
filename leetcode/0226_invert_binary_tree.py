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
    def invertTree(self, root):
        if root is None:
            return

        root.left, root.right = root.right, root.left
        if root.left is not None:
            root.left = self.invertTree(root.left)
        if root.right is not None:
            root.right = self.invertTree(root.right)
        return root


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(4)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(7)
    t0_3 = TreeNode(9)
    t0_4 = TreeNode(6)
    t0_5 = TreeNode(3)
    t0_6 = TreeNode(1)
    t0_2.left = t0_5
    t0_2.right = t0_6
    t0_1.left = t0_3
    t0_1.right = t0_4
    t0_0.left = t0_1
    t0_0.right = t0_2

    t1_0 = TreeNode(4)
    t1_1 = TreeNode(7)
    t1_2 = TreeNode(2)
    t1_3 = TreeNode(1)
    t1_4 = TreeNode(3)
    t1_5 = TreeNode(6)
    t1_6 = TreeNode(9)
    t1_2.left = t1_5
    t1_2.right = t1_6
    t1_1.left = t1_3
    t1_1.right = t1_4
    t1_0.left = t1_1
    t1_0.right = t1_2

    assert t1_0 == solution.invertTree(t0_0)
