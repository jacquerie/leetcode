# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        def _inorderTraversal(root):
            if root.left is not None:
                _inorderTraversal(root.left)
            result.append(root.val)
            if root.right is not None:
                _inorderTraversal(root.right)

        result = []
        if root is not None:
            _inorderTraversal(root)
        return result


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(3)
    t0_1.left = t0_2
    t0_0.right = t0_1

    assert [1, 3, 2] == solution.inorderTraversal(t0_0)
