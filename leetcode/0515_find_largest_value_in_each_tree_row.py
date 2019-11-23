# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestValues(self, root):
        result = []
        if root is None:
            return result

        current = [root]
        while current:
            result.append(max(node.val for node in current))
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
    t0_1 = TreeNode(3)
    t0_2 = TreeNode(2)
    t0_3 = TreeNode(5)
    t0_4 = TreeNode(3)
    t0_5 = TreeNode(9)
    t0_2.right = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert [1, 3, 9] == solution.largestValues(t0_0)
