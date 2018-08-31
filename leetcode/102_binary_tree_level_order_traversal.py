# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        result = []
        if root is None:
            return result

        current = [root]
        while current:
            result.append([node.val for node in current])
            next = []
            for node in current:
                if node.left is not None:
                    next.append(node.left)
                if node.right is not None:
                    next.append(node.right)
            current = next

        return result


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(3)
    t0_1 = TreeNode(9)
    t0_2 = TreeNode(20)
    t0_3 = TreeNode(15)
    t0_4 = TreeNode(7)
    t0_2.left = t0_3
    t0_2.right = t0_4
    t0_0.left = t0_1
    t0_0.right = t0_2

    assert [[3], [9, 20], [15, 7]] == solution.levelOrder(t0_0)
