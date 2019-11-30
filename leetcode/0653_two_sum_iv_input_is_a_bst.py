# -*- coding: utf-8 -*-

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root, k):
        stack = deque([root])
        while stack:
            node = stack.pop()
            if node.val != k - node.val and self.findNum(root, k - node.val):
                return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return False

    def findNum(self, root, num):
        if root.val == num:
            return True
        elif root.val > num and root.left:
            return self.findNum(root.left, num)
        elif root.val < num and root.right:
            return self.findNum(root.right, num)
        return False


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(5)
    t0_1 = TreeNode(3)
    t0_2 = TreeNode(6)
    t0_3 = TreeNode(2)
    t0_4 = TreeNode(4)
    t0_5 = TreeNode(7)
    t0_2.right = t0_5
    t0_1.left = t0_3
    t0_1.right = t0_4
    t0_0.left = t0_1
    t0_0.right = t0_2

    assert solution.findTarget(t0_0, 9)
    assert not solution.findTarget(t0_0, 28)

    t1_0 = TreeNode(1)

    assert not solution.findTarget(t1_0, 2)
