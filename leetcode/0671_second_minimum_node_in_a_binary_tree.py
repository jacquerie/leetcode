# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root):
        def _findSecondMinimumValue(root):
            if root is None:
                return [float("inf"), float("inf")]

            leftMins = _findSecondMinimumValue(root.left)
            rightMins = _findSecondMinimumValue(root.right)
            mins = sorted(set(leftMins + [root.val] + rightMins))

            return mins[:2]

        _, result = _findSecondMinimumValue(root)
        return result if result != float("inf") else -1


if __name__ == "__main__":
    solution = Solution()

    t0_0 = TreeNode(2)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(5)
    t0_3 = TreeNode(5)
    t0_4 = TreeNode(7)
    t0_2.right = t0_4
    t0_2.left = t0_3
    t0_0.right = t0_1
    t0_0.left = t0_2

    assert 5 == solution.findSecondMinimumValue(t0_0)

    t1_0 = TreeNode(2)
    t1_1 = TreeNode(2)
    t1_2 = TreeNode(2)
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert -1 == solution.findSecondMinimumValue(t1_0)
