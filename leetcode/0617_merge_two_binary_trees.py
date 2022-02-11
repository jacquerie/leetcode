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
    def mergeTrees(self, t1, t2):
        if t1 is None:
            return t2
        elif t2 is None:
            return t1

        result = TreeNode(t1.val + t2.val)
        result.left = self.mergeTrees(t1.left, t2.left)
        result.right = self.mergeTrees(t1.right, t2.right)

        return result


if __name__ == "__main__":
    solution = Solution()

    t1_0 = TreeNode(1)
    t1_1 = TreeNode(3)
    t1_2 = TreeNode(2)
    t1_3 = TreeNode(5)
    t1_1.left = t1_3
    t1_0.left = t1_1
    t1_0.right = t1_2

    t2_0 = TreeNode(2)
    t2_1 = TreeNode(1)
    t2_2 = TreeNode(3)
    t2_3 = TreeNode(4)
    t2_4 = TreeNode(7)
    t2_2.right = t2_4
    t2_1.right = t2_3
    t2_0.left = t2_1
    t2_0.right = t2_2

    t3_0 = TreeNode(3)
    t3_1 = TreeNode(4)
    t3_2 = TreeNode(5)
    t3_3 = TreeNode(5)
    t3_4 = TreeNode(4)
    t3_5 = TreeNode(7)
    t3_2.right = t3_5
    t3_1.left = t3_3
    t3_1.right = t3_4
    t3_0.left = t3_1
    t3_0.right = t3_2

    assert t3_0 == solution.mergeTrees(t1_0, t2_0)
