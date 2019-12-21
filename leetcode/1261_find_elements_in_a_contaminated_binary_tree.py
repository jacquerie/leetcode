# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements:
    def __init__(self, root: TreeNode):
        self.elements = set()
        self.build(root, 0)

    def build(self, root: TreeNode, current: int):
        if root is None:
            return
        self.elements.add(current)
        self.build(root.left, 2 * current + 1)
        self.build(root.right, 2 * current + 2)

    def find(self, target: int) -> bool:
        return target in self.elements


if __name__ == '__main__':
    t0_0 = TreeNode(-1)
    t0_1 = TreeNode(-1)
    t0_0.right = t0_1
    obj = FindElements(t0_0)
    assert not obj.find(1)
    assert obj.find(2)

    t1_0 = TreeNode(-1)
    t1_1 = TreeNode(-1)
    t1_2 = TreeNode(-1)
    t1_3 = TreeNode(-1)
    t1_4 = TreeNode(-1)
    t1_1.left = t1_3
    t1_1.right = t1_4
    t1_0.left = t1_1
    t1_0.right = t1_2
    obj = FindElements(t1_0)
    assert obj.find(1)
    assert obj.find(3)
    assert not obj.find(5)

    t2_0 = TreeNode(-1)
    t2_1 = TreeNode(-1)
    t2_2 = TreeNode(-1)
    t2_3 = TreeNode(-1)
    t2_2.left = t2_3
    t2_1.left = t2_2
    t2_0.right = t2_1
    obj = FindElements(t2_0)
    assert obj.find(2)
    assert not obj.find(3)
    assert not obj.find(4)
    assert obj.find(5)
