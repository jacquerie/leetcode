# -*- coding: utf-8 -*-

from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        diameter, _ = self.diameterAndHeightOfBinaryTree(root)

        return diameter - 1

    def diameterAndHeightOfBinaryTree(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if root is None:
            return (0, 0)

        left_diameter, left_height = self.diameterAndHeightOfBinaryTree(root.left)
        right_diameter, right_height = self.diameterAndHeightOfBinaryTree(root.right)

        diameter = max(left_diameter, right_diameter, left_height + right_height + 1)
        height = 1 + max(left_height, right_height)

        return (diameter, height)


if __name__ == '__main__':
    solution = Solution()

    t0_4 = TreeNode(5)
    t0_3 = TreeNode(4)
    t0_2 = TreeNode(3)
    t0_1 = TreeNode(2, t0_3, t0_4)
    t0_0 = TreeNode(1, t0_1, t0_2)
    assert 3 == solution.diameterOfBinaryTree(t0_0)

    t1_1 = TreeNode(2)
    t1_0 = TreeNode(1, t1_1)
    assert 1 == solution.diameterOfBinaryTree(t1_0)
