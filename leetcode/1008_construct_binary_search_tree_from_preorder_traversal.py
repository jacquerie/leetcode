# -*- coding: utf-8 -*-


class TreeNode:
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


class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None

        root, _ = self._bstFromPreorder(float('-inf'), float('inf'), 0, preorder)
        return root

    def _bstFromPreorder(self, minimum, maximum, index, preorder):
        if index == len(preorder):
            return None, index

        value = preorder[index]
        if value <= minimum or value >= maximum:
            return None, index

        node = TreeNode(value)
        node.left, index = self._bstFromPreorder(minimum, value, index + 1, preorder)
        node.right, index = self._bstFromPreorder(value, maximum, index, preorder)
        return node, index


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(8)
    t0_1 = TreeNode(5)
    t0_2 = TreeNode(10)
    t0_3 = TreeNode(1)
    t0_4 = TreeNode(7)
    t0_5 = TreeNode(12)
    t0_2.right = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert t0_0 == solution.bstFromPreorder([8, 5, 1, 7, 10, 12])
