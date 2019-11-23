# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Direction(object):
    LEFT = 0
    RIGHT = 1


class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        result = []
        direction = Direction.RIGHT

        current = [root]
        while current:
            if direction == Direction.RIGHT:
                result.append([node.val for node in current])
                direction = Direction.LEFT
            else:
                result.append([node.val for node in reversed(current)])
                direction = Direction.RIGHT
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

    assert [[3], [20, 9], [15, 7]] == solution.zigzagLevelOrder(t0_0)
