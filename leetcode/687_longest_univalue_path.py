# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        _, result = self._longestUnivaluePath(root)
        return result

    def _longestUnivaluePath(self, root):
        if root is None:
            return 0, 0

        leftLength, leftResult = self._longestUnivaluePath(root.left)
        rightLength, rightResult = self._longestUnivaluePath(root.right)

        leftLength = leftLength + 1 if root.left and root.val == root.left.val else 0
        rightLength = rightLength + 1 if root.right and root.val == root.right.val else 0

        length = max(leftLength, rightLength)
        result = max(leftResult, rightResult, leftLength + rightLength)

        return length, result


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(5)
    t0_1 = TreeNode(4)
    t0_2 = TreeNode(5)
    t0_3 = TreeNode(1)
    t0_4 = TreeNode(1)
    t0_5 = TreeNode(5)
    t0_2.left = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert 2 == solution.longestUnivaluePath(t0_0)

    t1_0 = TreeNode(1)
    t1_1 = TreeNode(4)
    t1_2 = TreeNode(5)
    t1_3 = TreeNode(4)
    t1_4 = TreeNode(4)
    t1_5 = TreeNode(5)
    t1_2.left = t1_5
    t1_1.right = t1_4
    t1_1.left = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert 2 == solution.longestUnivaluePath(t1_0)
