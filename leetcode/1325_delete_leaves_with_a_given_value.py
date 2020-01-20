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
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root is None:
            return None
        return self._removeLeafNodes(root, target)

    def _removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root.left is not None:
            root.left = self._removeLeafNodes(root.left, target)
        if root.right is not None:
            root.right = self._removeLeafNodes(root.right, target)
        if root.left is None and root.val == target and root.right is None:
            return None
        return root


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(3)
    t0_3 = TreeNode(2)
    t0_4 = TreeNode(2)
    t0_5 = TreeNode(4)
    t0_2.right = t0_5
    t0_2.left = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    t1_0 = TreeNode(1)
    t1_1 = TreeNode(3)
    t1_2 = TreeNode(4)
    t1_1.right = t1_2
    t1_0.right = t1_1

    assert t1_0 == solution.removeLeafNodes(t0_0, 2)

    t2_0 = TreeNode(1)
    t2_1 = TreeNode(3)
    t2_2 = TreeNode(3)
    t2_3 = TreeNode(3)
    t2_4 = TreeNode(2)
    t2_1.right = t2_4
    t2_1.left = t2_3
    t2_0.right = t2_2
    t2_0.left = t2_1

    t3_0 = TreeNode(1)
    t3_1 = TreeNode(3)
    t3_2 = TreeNode(2)
    t3_1.right = t3_2
    t3_0.left = t3_1

    assert t3_0 == solution.removeLeafNodes(t2_0, 3)

    t4_0 = TreeNode(1)
    t4_1 = TreeNode(2)
    t4_2 = TreeNode(2)
    t4_3 = TreeNode(2)
    t4_2.left = t4_3
    t4_1.left = t4_2
    t4_0.left = t4_1

    t5_0 = TreeNode(1)

    assert t5_0 == solution.removeLeafNodes(t4_0, 2)

    t6_0 = TreeNode(1)
    t6_1 = TreeNode(1)
    t6_2 = TreeNode(1)
    t6_0.right = t6_2
    t6_0.left = t6_1

    t7_0 = None

    assert t7_0 == solution.removeLeafNodes(t6_0, 1)

    t8_0 = TreeNode(1)
    t8_1 = TreeNode(2)
    t8_2 = TreeNode(3)
    t8_0.right = t8_2
    t8_0.left = t8_1

    t9_0 = TreeNode(1)
    t9_1 = TreeNode(2)
    t9_2 = TreeNode(3)
    t9_0.right = t9_2
    t9_0.left = t9_1

    assert t9_0 == solution.removeLeafNodes(t8_0, 1)
