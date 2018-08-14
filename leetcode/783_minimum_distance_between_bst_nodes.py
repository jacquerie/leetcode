# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDiffInBST(self, root):
        def _inOrderTraversal(root, previous, result):
            if root is None:
                return previous, result

            previous, result = _inOrderTraversal(root.left, previous, result)
            if previous:
                result = min(result, root.val - previous.val)
            return _inOrderTraversal(root.right, root, result)

        _, result = _inOrderTraversal(root, None, float('inf'))
        return result


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(4)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(6)
    t0_3 = TreeNode(1)
    t0_4 = TreeNode(3)
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert 1 == solution.minDiffInBST(t0_0)
