# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)

        current = root
        while True:
            if current.val < val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    break
            else:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    break

        return root


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(4)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(7)
    t0_3 = TreeNode(1)
    t0_4 = TreeNode(3)

    t1_0 = TreeNode(4)
    t1_1 = TreeNode(2)
    t1_2 = TreeNode(7)
    t1_3 = TreeNode(1)
    t1_4 = TreeNode(3)
    t1_5 = TreeNode(5)

    assert t1_0 == solution.insertIntoBST(t0_0, 5)
