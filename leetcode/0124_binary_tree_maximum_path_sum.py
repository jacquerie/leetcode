# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        _, result = self._maxPathSum(root)
        return result

    def _maxPathSum(self, root):
        if root is None:
            return 0, float("-inf")

        leftMaxPathSum, leftResult = self._maxPathSum(root.left)
        rightMaxPathSum, rightResult = self._maxPathSum(root.right)

        maxPathSum = max(max(leftMaxPathSum, rightMaxPathSum) + root.val, 0)
        result = max(
            leftResult, leftMaxPathSum + root.val + rightMaxPathSum, rightResult
        )

        return maxPathSum, result


if __name__ == "__main__":
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(3)
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert 6 == solution.maxPathSum(t0_0)

    t1_0 = TreeNode(-10)
    t1_1 = TreeNode(9)
    t1_2 = TreeNode(20)
    t1_3 = TreeNode(15)
    t1_4 = TreeNode(7)
    t1_2.right = t1_4
    t1_2.left = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert 42 == solution.maxPathSum(t1_0)

    t2_0 = TreeNode(-3)

    assert -3 == solution.maxPathSum(t2_0)

    t3_0 = TreeNode(5)
    t3_1 = TreeNode(4)
    t3_2 = TreeNode(8)
    t3_3 = TreeNode(11)
    t3_4 = TreeNode(13)
    t3_5 = TreeNode(4)
    t3_6 = TreeNode(7)
    t3_7 = TreeNode(2)
    t3_8 = TreeNode(1)
    t3_5.right = t3_8
    t3_3.right = t3_7
    t3_3.left = t3_6
    t3_2.right = t3_5
    t3_2.left = t3_4
    t3_1.left = t3_3
    t3_0.right = t3_2
    t3_0.left = t3_1

    assert 48 == solution.maxPathSum(t3_0)

    t4_0 = TreeNode(2)
    t4_1 = TreeNode(-1)
    t4_0.left = t4_1

    assert 2 == solution.maxPathSum(t4_0)
