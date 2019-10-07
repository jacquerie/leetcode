# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumRootToLeaf(self, root):
        return self._sumRootToLeaf(root, 0)

    def _sumRootToLeaf(self, root, current):
        current = 2 * current + root.val

        if root.left is None and root.right is None:
            return current
        elif root.left is None:
            return self._sumRootToLeaf(root.right, current)
        elif root.right is None:
            return self._sumRootToLeaf(root.left, current)
        return self._sumRootToLeaf(root.left, current) + self._sumRootToLeaf(root.right, current)


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(0)
    t0_2 = TreeNode(1)
    t0_3 = TreeNode(0)
    t0_4 = TreeNode(1)
    t0_5 = TreeNode(0)
    t0_6 = TreeNode(1)
    t0_2.right = t0_6
    t0_2.left = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert 22 == solution.sumRootToLeaf(t0_0)
