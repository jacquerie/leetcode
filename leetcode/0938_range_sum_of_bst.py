# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root, L, R):
        if root is None:
            return 0

        result = 0

        if L <= root.val <= R:
            result += root.val
        if L <= root.val:
            result += self.rangeSumBST(root.left, L, R)
        if root.val <= R:
            result += self.rangeSumBST(root.right, L, R)

        return result


if __name__ == "__main__":
    solution = Solution()

    t0_0 = TreeNode(10)
    t0_1 = TreeNode(5)
    t0_2 = TreeNode(15)
    t0_3 = TreeNode(3)
    t0_4 = TreeNode(7)
    t0_5 = TreeNode(18)
    t0_2.right = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert 32 == solution.rangeSumBST(t0_0, 7, 15)

    t1_0 = TreeNode(10)
    t1_1 = TreeNode(5)
    t1_2 = TreeNode(15)
    t1_3 = TreeNode(3)
    t1_4 = TreeNode(7)
    t1_5 = TreeNode(13)
    t1_6 = TreeNode(18)
    t1_7 = TreeNode(1)
    t1_8 = TreeNode(6)
    t1_4.left = t1_8
    t1_3.left = t1_7
    t1_2.right = t1_6
    t1_2.left = t1_5
    t1_1.right = t1_4
    t1_1.left = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert 23 == solution.rangeSumBST(t1_0, 6, 10)
