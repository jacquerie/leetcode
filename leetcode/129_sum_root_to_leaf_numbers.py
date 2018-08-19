# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        result = 0
        if root is None:
            return result

        for path in self.allPaths(root):
            result += self.sumPath(path)

        return result

    def allPaths(self, root):
        if root.left is None and root.right is None:
            return [[root.val]]

        result = []

        if root.left is not None:
            for path in self.allPaths(root.left):
                path.append(root.val)
                result.append(path)
        if root.right is not None:
            for path in self.allPaths(root.right):
                path.append(root.val)
                result.append(path)

        return result

    def sumPath(self, path):
        result = 0

        for el in reversed(path):
            result *= 10
            result += el

        return result


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
