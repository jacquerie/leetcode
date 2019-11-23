# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flipEquiv(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        return (
            root1.val == root2.val and (
                ((self.flipEquiv(root1.left, root2.left) and
                  self.flipEquiv(root1.right, root2.right))) or
                ((self.flipEquiv(root1.left, root2.right) and
                  self.flipEquiv(root1.right, root2.left)))
            )
        )


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(3)
    t0_3 = TreeNode(4)
    t0_4 = TreeNode(5)
    t0_5 = TreeNode(6)
    t0_6 = TreeNode(7)
    t0_7 = TreeNode(8)
    t0_4.right = t0_7
    t0_4.left = t0_6
    t0_2.left = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    t1_0 = TreeNode(1)
    t1_1 = TreeNode(3)
    t1_2 = TreeNode(2)
    t1_3 = TreeNode(6)
    t1_4 = TreeNode(4)
    t1_5 = TreeNode(5)
    t1_6 = TreeNode(8)
    t1_7 = TreeNode(7)
    t1_5.right = t1_7
    t1_5.left = t1_6
    t1_2.right = t1_5
    t1_2.left = t1_4
    t1_1.right = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert solution.flipEquiv(t0_0, t1_0)
