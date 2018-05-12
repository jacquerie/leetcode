# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        return (
            p.val == q.val and
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(3)
    t0_0.left = t0_1
    t0_0.right = t0_2

    t1_0 = TreeNode(1)
    t1_1 = TreeNode(2)
    t1_2 = TreeNode(3)
    t1_0.left = t1_1
    t1_0.right = t1_2

    assert solution.isSameTree(t0_0, t1_0)
