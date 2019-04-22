# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        def _isBalanced(root, depth):
            if root is None:
                return True, depth

            leftBalanced, leftDepth = _isBalanced(root.left, depth)
            rightBalanced, rightDepth = _isBalanced(root.right, depth)

            balanced = leftBalanced and rightBalanced and abs(leftDepth - rightDepth) <= 1
            depth = 1 + max(leftDepth, rightDepth)

            return balanced, depth

        result, _ = _isBalanced(root, 0)
        return result


if __name__ == '__main__':
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

    assert solution.isBalanced(t0_0)

    t1_0 = TreeNode(1)
    t1_1 = TreeNode(2)
    t1_0.left = t1_1

    assert solution.isBalanced(t1_0)
