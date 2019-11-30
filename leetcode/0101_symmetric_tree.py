# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, left, right):
        if left is None or right is None:
            return left is None and right is None
        return (
            left.val == right.val and
            self._isSymmetric(left.left, right.right) and
            self._isSymmetric(left.right, right.left)
        )


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(2)
    t0_3 = TreeNode(3)
    t0_4 = TreeNode(4)
    t0_5 = TreeNode(4)
    t0_6 = TreeNode(3)
    t0_2.left = t0_5
    t0_2.right = t0_6
    t0_1.left = t0_3
    t0_1.right = t0_4
    t0_0.left = t0_1
    t0_0.right = t0_2

    assert solution.isSymmetric(t0_0)

    t1_0 = TreeNode(1)
    t1_1 = TreeNode(2)
    t1_2 = TreeNode(2)
    t1_3 = TreeNode(3)
    t1_4 = TreeNode(3)
    t1_2.right = t1_4
    t1_1.right = t1_3
    t1_0.left = t1_1
    t1_0.right = t1_2

    assert not solution.isSymmetric(t1_0)
