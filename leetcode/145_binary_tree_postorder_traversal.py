# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        def _postorderTraversal(root):
            if root.left is not None:
                _postorderTraversal(root.left)
            if root.right is not None:
                _postorderTraversal(root.right)
            result.append(root.val)

        result = []
        if root is not None:
            _postorderTraversal(root)
        return result


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(3)
    t0_1.left = t0_2
    t0_0.right = t0_1

    assert [3, 2, 1] == solution.postorderTraversal(t0_0)
