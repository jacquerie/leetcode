# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        result = []
        if root is None:
            return result

        for path in self.allPaths(root):
            if sum == self.sumPath(path):
                result.append(list(reversed(path)))

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
        return sum(path)


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(5)
    t0_1 = TreeNode(4)
    t0_2 = TreeNode(8)
    t0_3 = TreeNode(11)
    t0_4 = TreeNode(13)
    t0_5 = TreeNode(4)
    t0_6 = TreeNode(7)
    t0_7 = TreeNode(2)
    t0_8 = TreeNode(5)
    t0_9 = TreeNode(1)
    t0_5.right = t0_9
    t0_5.left = t0_8
    t0_3.right = t0_7
    t0_3.left = t0_6
    t0_2.right = t0_5
    t0_2.left = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert [[5, 4, 11, 2], [5, 8, 4, 5]] == solution.pathSum(t0_0, 22)
