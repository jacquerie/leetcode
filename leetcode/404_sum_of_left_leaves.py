# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        def _sumOfLeftLeaves(root, is_left=False):
            if root is None:
                return 0
            elif root.left is None and root.right is None and is_left:
                return root.val
            return _sumOfLeftLeaves(root.left, is_left=True) + _sumOfLeftLeaves(root.right)

        return _sumOfLeftLeaves(root)


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

    assert 24 == solution.sumOfLeftLeaves(t0_0)
