# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        def _inorderTraversal(root, result):
            if root.left is not None:
                _inorderTraversal(root.left, result)
            result.append(root.val)
            if root.right is not None:
                _inorderTraversal(root.right, result)

        result = []
        _inorderTraversal(root, result)
        return result[k - 1]


if __name__ == "__main__":
    solution = Solution()

    t0_0 = TreeNode(3)
    t0_1 = TreeNode(1)
    t0_2 = TreeNode(4)
    t0_3 = TreeNode(2)
    t0_1.right = t0_3
    t0_0.left = t0_1
    t0_0.right = t0_2

    assert 1 == solution.kthSmallest(t0_0, 1)
