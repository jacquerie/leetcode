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
    def buildTree(self, preorder, inorder):
        inorderLookup = self._buildInorderLookup(inorder)
        return self._buildTree(inorderLookup, preorder, 0, 0, len(inorder))

    def _buildInorderLookup(self, inorder):
        result = {}
        for i, el in enumerate(inorder):
            result[el] = i
        return result

    def _buildTree(self, lookup, preorder, i, in_start, in_end):
        if in_start == in_end:
            return None

        j = lookup[preorder[i]]

        node = TreeNode(preorder[i])
        node.left = self._buildTree(lookup, preorder, i + 1, in_start, j)
        node.right = self._buildTree(lookup, preorder, i + 1 + j - in_start, j + 1, in_end)

        return node


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(3)
    t0_1 = TreeNode(9)
    t0_2 = TreeNode(20)
    t0_3 = TreeNode(15)
    t0_4 = TreeNode(7)
    t0_2.right = t0_4
    t0_2.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert t0_0 == solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
