# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        if root is None:
            return True
        return self._isUnivalTree(root, root.val)

    def _isUnivalTree(self, root, val):
        result = root.val == val
        if root.left is not None:
            result = result and self._isUnivalTree(root.left, val)
        if root.right is not None:
            result = result and self._isUnivalTree(root.right, val)
        return result


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(1)
    t0_2 = TreeNode(1)
    t0_3 = TreeNode(1)
    t0_4 = TreeNode(1)
    t0_5 = TreeNode(1)
    t0_2.right = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert solution.isUnivalTree(t0_0)

    t1_0 = TreeNode(2)
    t1_1 = TreeNode(2)
    t1_2 = TreeNode(2)
    t1_3 = TreeNode(5)
    t1_4 = TreeNode(2)
    t1_1.right = t1_4
    t1_1.left = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert not solution.isUnivalTree(t1_0)
