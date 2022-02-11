# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self._sumEvenGrandparent(root, -1, -1)

    def _sumEvenGrandparent(self, root: TreeNode, parent: int, grandparent: int) -> int:
        if root is None:
            return 0
        return (
            self._sumEvenGrandparent(root.left, root.val, parent)
            + self._sumEvenGrandparent(root.right, root.val, parent)
            + (root.val if grandparent % 2 == 0 else 0)
        )


if __name__ == "__main__":
    solution = Solution()

    t0_0 = TreeNode(6)
    t0_1 = TreeNode(7)
    t0_2 = TreeNode(8)
    t0_3 = TreeNode(2)
    t0_4 = TreeNode(7)
    t0_5 = TreeNode(1)
    t0_6 = TreeNode(3)
    t0_7 = TreeNode(9)
    t0_8 = TreeNode(1)
    t0_9 = TreeNode(4)
    t0_10 = TreeNode(5)
    t0_6.right = t0_10
    t0_4.right = t0_9
    t0_4.left = t0_8
    t0_3.left = t0_7
    t0_2.right = t0_6
    t0_2.left = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert 18 == solution.sumEvenGrandparent(t0_0)
