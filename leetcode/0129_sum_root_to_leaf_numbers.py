# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        if root is None:
            return 0
        return self._sumNumbers(root, 0)

    def _sumNumbers(self, root, current):
        current = 10 * current + root.val

        if root.left is None and root.right is None:
            return current
        elif root.left is None:
            return self._sumNumbers(root.right, current)
        elif root.right is None:
            return self._sumNumbers(root.left, current)
        return self._sumNumbers(root.left, current) + self._sumNumbers(root.right, current)


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(3)
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert 25 == solution.sumNumbers(t0_0)

    t1_0 = TreeNode(4)
    t1_1 = TreeNode(9)
    t1_2 = TreeNode(0)
    t1_3 = TreeNode(5)
    t1_4 = TreeNode(1)
    t1_1.right = t1_4
    t1_1.left = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert 1026 == solution.sumNumbers(t1_0)

    t2_0 = None

    assert 0 == solution.sumNumbers(t2_0)
