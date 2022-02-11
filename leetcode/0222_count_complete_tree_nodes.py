# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root):
        if root is None:
            return 0

        depth = self.getDepth(root)

        first, last = 1, 2**depth
        while first < last:
            mid = (first + last) // 2
            if self.exists(root, mid, depth):
                first = mid + 1
            else:
                last = mid

        return 2**depth + first - 1

    def getDepth(self, root):
        current, depth = root, 0
        while current.left is not None:
            current, depth = current.left, depth + 1
        return depth

    def exists(self, root, value, depth):
        current = root
        for bit in self.toBinary(value, depth):
            if bit == "0" and current.left is not None:
                current = current.left
            elif bit == "1" and current.right is not None:
                current = current.right
            else:
                return False
        return True

    def toBinary(self, value, depth):
        return bin(value)[2:].zfill(depth)


if __name__ == "__main__":
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

    assert 6 == solution.countNodes(t0_0)

    t1_0 = TreeNode(1)

    assert 1 == solution.countNodes(t1_0)
