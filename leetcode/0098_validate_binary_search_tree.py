# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        return self._isValidBST(root, float('-inf'), float('inf'))

    def _isValidBST(self, root, minimum, maximum):
        if root is None:
            return True
        return (
            minimum < root.val < maximum and
            self._isValidBST(root.left, minimum, root.val) and
            self._isValidBST(root.right, root.val, maximum)
        )


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(2)
    t0_1 = TreeNode(1)
    t0_2 = TreeNode(3)
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert solution.isValidBST(t0_0)

    t1_0 = TreeNode(5)
    t1_1 = TreeNode(1)
    t1_2 = TreeNode(4)
    t1_3 = TreeNode(3)
    t1_4 = TreeNode(6)
    t1_2.right = t1_4
    t1_2.left = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert not solution.isValidBST(t1_0)

    t2_0 = TreeNode(2147483647)

    assert solution.isValidBST(t2_0)
