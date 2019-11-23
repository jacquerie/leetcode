# -*- coding: utf-8 -*-


class TreeNode(object):
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


class Solution(object):
    def flatten(self, root):
        self._flatten(root, None)

    def _flatten(self, root, result):
        if root is None:
            return result

        result = self._flatten(root.right, result)
        result = self._flatten(root.left, result)

        root.left = None
        root.right = result

        return root


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(5)
    t0_3 = TreeNode(3)
    t0_4 = TreeNode(4)
    t0_5 = TreeNode(6)
    t0_2.right = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    t1_0 = TreeNode(1)
    t1_1 = TreeNode(2)
    t1_2 = TreeNode(3)
    t1_3 = TreeNode(4)
    t1_4 = TreeNode(5)
    t1_5 = TreeNode(6)
    t1_4.right = t1_5
    t1_3.right = t1_4
    t1_2.right = t1_3
    t1_1.right = t1_2
    t1_0.right = t1_1

    assert solution.flatten(t0_0) is None
    assert t1_0 == t0_0
