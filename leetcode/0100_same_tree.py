# -*- coding: utf-8 -*-

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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

    t0_2 = TreeNode(3)
    t0_1 = TreeNode(2)
    t0_0 = TreeNode(1, t0_1, t0_2)

    t1_2 = TreeNode(3)
    t1_1 = TreeNode(2)
    t1_0 = TreeNode(1, t1_1, t1_2)

    assert solution.isSameTree(t0_0, t1_0)
