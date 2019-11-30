# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        result, _ = self._pathSum(root, sum)
        return result

    def _pathSum(self, root, sum):
        if root is None:
            return 0, []

        leftResult, leftPathSums = self._pathSum(root.left, sum)
        rightResult, rightPathSums = self._pathSum(root.right, sum)

        result = leftResult + rightResult + (1 if root.val == sum else 0)
        pathSums = [root.val]

        for leftPathSum in leftPathSums:
            pathSums.append(leftPathSum + root.val)
            if leftPathSum + root.val == sum:
                result += 1

        for rightPathSum in rightPathSums:
            pathSums.append(root.val + rightPathSum)
            if root.val + rightPathSum == sum:
                result += 1

        return result, pathSums


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(10)
    t0_1 = TreeNode(5)
    t0_2 = TreeNode(-3)
    t0_3 = TreeNode(3)
    t0_4 = TreeNode(2)
    t0_5 = TreeNode(11)
    t0_6 = TreeNode(3)
    t0_7 = TreeNode(-2)
    t0_8 = TreeNode(1)
    t0_4.right = t0_8
    t0_3.right = t0_7
    t0_3.left = t0_6
    t0_2.right = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert 3 == solution.pathSum(t0_0, 8)
