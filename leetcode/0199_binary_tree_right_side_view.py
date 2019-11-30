# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root):
        if root is None:
            return []

        result = []

        current = [root]
        while current:
            result.append(current[-1].val)
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

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(3)
    t0_3 = TreeNode(5)
    t0_4 = TreeNode(4)
    t0_2.right = t0_4
    t0_1.right = t0_3
    t0_0.left = t0_1
    t0_0.right = t0_2

    assert [1, 3, 4] == solution.rightSideView(t0_0)
