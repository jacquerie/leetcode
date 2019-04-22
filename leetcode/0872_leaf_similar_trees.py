# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def leafSimilar(self, root1, root2):
        leaves1, leaves2 = [], []
        self._leafSimilar(root1, leaves1)
        self._leafSimilar(root2, leaves2)

        return leaves1 == leaves2

    def _leafSimilar(self, root, leaves):
        if root is None:
            return
        elif root.left is None and root.right is None:
            leaves.append(root.val)
        else:
            self._leafSimilar(root.left, leaves)
            self._leafSimilar(root.right, leaves)


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(3)
    t0_1 = TreeNode(5)
    t0_2 = TreeNode(1)
    t0_3 = TreeNode(6)
    t0_4 = TreeNode(2)
    t0_5 = TreeNode(9)
    t0_6 = TreeNode(8)
    t0_7 = TreeNode(7)
    t0_8 = TreeNode(4)
    t0_4.right = t0_8
    t0_4.left = t0_7
    t0_2.right = t0_6
    t0_2.left = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    t1_0 = TreeNode(3)
    t1_1 = TreeNode(5)
    t1_2 = TreeNode(1)
    t1_3 = TreeNode(6)
    t1_4 = TreeNode(7)
    t1_5 = TreeNode(2)
    t1_6 = TreeNode(8)
    t1_7 = TreeNode(4)
    t1_8 = TreeNode(9)
    t1_5.right = t1_8
    t1_5.left = t1_7
    t1_2.right = t1_6
    t1_2.left = t1_5
    t1_1.right = t1_4
    t1_1.left = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert solution.leafSimilar(t0_0, t1_0)
