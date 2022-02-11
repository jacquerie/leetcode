# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        return (
            other is not None
            and self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )


class Solution:
    def convertBST(self, root):
        self._convertBST(root, 0)
        return root

    def _convertBST(self, root, current_sum):
        if root is None:
            return current_sum

        if root.right is not None:
            current_sum = self._convertBST(root.right, current_sum)
        current_sum += root.val
        root.val = current_sum
        if root.left is not None:
            current_sum = self._convertBST(root.left, current_sum)

        return current_sum


if __name__ == "__main__":
    solution = Solution()

    t0_0 = TreeNode(5)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(13)
    t0_0.right = t0_2
    t0_0.left = t0_1

    t1_0 = TreeNode(18)
    t1_1 = TreeNode(20)
    t1_2 = TreeNode(13)
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert t1_0 == solution.convertBST(t0_0)
