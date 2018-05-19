# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import operator


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
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None

        i, maximum = max(enumerate(nums), key=operator.itemgetter(1))
        node = TreeNode(maximum)
        node.left = self.constructMaximumBinaryTree(nums[:i])
        node.right = self.constructMaximumBinaryTree(nums[i+1:])

        return node


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(6)
    t0_1 = TreeNode(3)
    t0_2 = TreeNode(5)
    t0_3 = TreeNode(2)
    t0_4 = TreeNode(0)
    t0_5 = TreeNode(1)
    t0_3.right = t0_5
    t0_2.left = t0_4
    t0_1.right = t0_3
    t0_0.left = t0_1
    t0_0.right = t0_2

    assert t0_0 == solution.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
