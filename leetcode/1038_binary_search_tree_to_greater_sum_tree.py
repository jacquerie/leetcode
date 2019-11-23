# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        return (
            other is not None and
            self.val == other.val and
            self.left == other.left and
            self.right == other.right
        )


class Solution(object):
    def bstToGst(self, root):
        self._bstToGst(root, 0)
        return root

    def _bstToGst(self, node, current_sum):
        if node is None:
            return current_sum
        node.val += self._bstToGst(node.right, current_sum)
        return self._bstToGst(node.left, node.val)


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(4)
    t0_1 = TreeNode(1)
    t0_2 = TreeNode(6)
    t0_3 = TreeNode(0)
    t0_4 = TreeNode(2)
    t0_5 = TreeNode(5)
    t0_6 = TreeNode(7)
    t0_7 = TreeNode(3)
    t0_8 = TreeNode(8)
    t0_6.right = t0_8
    t0_4.right = t0_7
    t0_2.right = t0_6
    t0_2.left = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    t1_0 = TreeNode(30)
    t1_1 = TreeNode(36)
    t1_2 = TreeNode(21)
    t1_3 = TreeNode(36)
    t1_4 = TreeNode(35)
    t1_5 = TreeNode(26)
    t1_6 = TreeNode(15)
    t1_7 = TreeNode(33)
    t1_8 = TreeNode(8)
    t1_6.right = t1_8
    t1_4.right = t1_7
    t1_2.right = t1_6
    t1_2.left = t1_5
    t1_1.right = t1_4
    t1_1.left = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert t1_0 == solution.bstToGst(t0_0)
