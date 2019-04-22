# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        if s is None and t is None:
            return True
        elif s is None and t is not None:
            return False
        elif s is not None and t is None:
            return True
        elif self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, s, t):
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        return (
            s.val == t.val and
            self.isSameTree(s.left, t.left) and
            self.isSameTree(s.right, t.right)
        )


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(3)
    t0_1 = TreeNode(4)
    t0_2 = TreeNode(5)
    t0_3 = TreeNode(1)
    t0_4 = TreeNode(2)
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    t1_0 = TreeNode(4)
    t1_1 = TreeNode(1)
    t1_2 = TreeNode(2)
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert solution.isSubtree(t0_0, t1_0)

    t2_0 = TreeNode(3)
    t2_1 = TreeNode(4)
    t2_2 = TreeNode(5)
    t2_3 = TreeNode(1)
    t2_4 = TreeNode(2)
    t2_5 = TreeNode(0)
    t2_4.left = t2_5
    t2_1.right = t2_4
    t2_1.left = t2_3
    t2_0.right = t2_2
    t2_0.left = t2_1

    assert not solution.isSubtree(t2_0, t1_0)
