# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
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


class Solution(object):
    def increasingBST(self, root):
        return self._increasingBST(root, None)

    def _increasingBST(self, root, rest):
        if root is None:
            return rest

        result = self._increasingBST(root.left, root)

        root.left = None
        root.right = self._increasingBST(root.right, rest)

        return result


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(5)
    t0_1 = TreeNode(3)
    t0_2 = TreeNode(6)
    t0_3 = TreeNode(2)
    t0_4 = TreeNode(4)
    t0_5 = TreeNode(8)
    t0_6 = TreeNode(1)
    t0_7 = TreeNode(7)
    t0_8 = TreeNode(9)
    t0_5.right = t0_8
    t0_5.left = t0_7
    t0_3.left = t0_6
    t0_2.right = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    t1_0 = TreeNode(1)
    t1_1 = TreeNode(2)
    t1_2 = TreeNode(3)
    t1_3 = TreeNode(4)
    t1_4 = TreeNode(5)
    t1_5 = TreeNode(6)
    t1_6 = TreeNode(7)
    t1_7 = TreeNode(8)
    t1_8 = TreeNode(9)
    t1_7.right = t1_8
    t1_6.right = t1_7
    t1_5.right = t1_6
    t1_4.right = t1_5
    t1_3.right = t1_4
    t1_2.right = t1_3
    t1_1.right = t1_2
    t1_0.right = t1_1

    assert t1_0 == solution.increasingBST(t0_0)
