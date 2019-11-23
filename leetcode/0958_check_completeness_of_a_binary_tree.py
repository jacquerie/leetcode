# -*- coding: utf-8 -*-

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isCompleteTree(self, root):
        if not root:
            return True

        queue = deque([root])
        last_level = False

        while queue:
            node = queue.popleft()

            if last_level and (node.left or node.right):
                return False
            elif not node.right:
                last_level = True
            elif not node.left:
                return False

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return True


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(3)
    t0_3 = TreeNode(4)
    t0_4 = TreeNode(5)
    t0_5 = TreeNode(6)
    t0_2.left = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert solution.isCompleteTree(t0_0)

    t1_0 = TreeNode(1)
    t1_1 = TreeNode(2)
    t1_2 = TreeNode(3)
    t1_3 = TreeNode(4)
    t1_4 = TreeNode(5)
    t1_5 = TreeNode(7)
    t1_2.right = t1_5
    t1_1.right = t1_4
    t1_1.left = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert not solution.isCompleteTree(t1_0)
