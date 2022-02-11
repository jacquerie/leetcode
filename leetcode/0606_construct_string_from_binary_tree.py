# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t):
        if t is None:
            return ""

        result = [str(t.val)]
        if t.left is not None or t.right is not None:
            result.extend(["(", self.tree2str(t.left), ")"])
        if t.right is not None:
            result.extend(["(", self.tree2str(t.right), ")"])

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(3)
    t0_3 = TreeNode(4)
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert "1(2(4))(3)" == solution.tree2str(t0_0)

    t1_0 = TreeNode(1)
    t1_1 = TreeNode(2)
    t1_2 = TreeNode(3)
    t1_3 = TreeNode(4)
    t1_1.right = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert "1(2()(4))(3)" == solution.tree2str(t1_0)
