# -*- coding: utf-8 -*-

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = []
        self.inorderTraversal(root1, result)
        self.inorderTraversal(root2, result)
        return list(sorted(result))

    def inorderTraversal(self, root: TreeNode, result: List[int]):
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.val)
            self.inorderTraversal(root.right, result)


if __name__ == "__main__":
    solution = Solution()

    t0_0 = TreeNode(2)
    t0_1 = TreeNode(1)
    t0_2 = TreeNode(4)
    t0_0.right = t0_2
    t0_0.left = t0_1

    t1_0 = TreeNode(1)
    t1_1 = TreeNode(0)
    t1_2 = TreeNode(3)
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert [0, 1, 1, 2, 3, 4] == solution.getAllElements(t0_0, t1_0)

    t2_0 = TreeNode(0)
    t2_1 = TreeNode(-10)
    t2_2 = TreeNode(10)
    t2_0.right = t2_2
    t2_0.left = t2_1

    t3_0 = TreeNode(5)
    t3_1 = TreeNode(1)
    t3_2 = TreeNode(7)
    t3_3 = TreeNode(0)
    t3_4 = TreeNode(2)
    t3_1.right = t3_4
    t3_1.left = t3_3
    t3_0.right = t3_2
    t3_0.left = t3_1

    assert [-10, 0, 0, 1, 2, 5, 7, 10] == solution.getAllElements(t2_0, t3_0)

    t4_0 = None

    t5_0 = TreeNode(5)
    t5_1 = TreeNode(1)
    t5_2 = TreeNode(7)
    t5_3 = TreeNode(0)
    t5_4 = TreeNode(2)
    t5_1.right = t5_4
    t5_1.left = t5_3
    t5_0.right = t5_2
    t5_0.left = t5_1

    assert [0, 1, 2, 5, 7] == solution.getAllElements(t4_0, t5_0)

    t6_0 = TreeNode(0)
    t6_1 = TreeNode(-10)
    t6_2 = TreeNode(10)
    t6_0.right = t6_2
    t6_0.left = t6_1

    t7_0 = None

    assert [-10, 0, 10] == solution.getAllElements(t6_0, t7_0)

    t8_0 = TreeNode(1)
    t8_1 = TreeNode(8)
    t8_0.right = t8_1

    t9_0 = TreeNode(8)
    t9_1 = TreeNode(1)
    t9_0.left = t9_1

    assert [1, 1, 8, 8] == solution.getAllElements(t8_0, t9_0)
