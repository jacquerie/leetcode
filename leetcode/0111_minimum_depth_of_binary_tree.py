# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        elif root.left is None:
            return 1 + self.minDepth(root.right)
        elif root.right is None:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


if __name__ == "__main__":
    solution = Solution()

    t0_0 = TreeNode(3)
    t0_1 = TreeNode(9)
    t0_2 = TreeNode(20)
    t0_3 = TreeNode(15)
    t0_4 = TreeNode(7)
    t0_2.left = t0_3
    t0_2.right = t0_4
    t0_0.left = t0_1
    t0_0.right = t0_2

    assert 2 == solution.minDepth(t0_0)

    t1_0 = TreeNode(1)
    t1_1 = TreeNode(2)
    t1_0.left = t1_1

    assert 2 == solution.minDepth(t1_0)

    t2_0 = TreeNode(1)
    t2_1 = TreeNode(2)
    t2_2 = TreeNode(3)
    t2_1.right = t2_2
    t2_0.left = t2_1

    assert 3 == solution.minDepth(t2_0)
