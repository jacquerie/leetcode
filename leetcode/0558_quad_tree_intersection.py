# -*- coding: utf-8 -*-


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def __eq__(self, other):
        return (
            other is not None and
            self.val == other.val and
            self.isLeaf == other.isLeaf and
            self.topLeft == other.topLeft and
            self.topRight == other.topRight and
            self.bottomLeft == other.bottomLeft and
            self.bottomRight == other.bottomRight
        )


class Solution:
    def intersect(self, quadTree1, quadTree2):
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        elif quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1

        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
            if topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, True, None, None, None, None)
        return Node(None, False, topLeft, topRight, bottomLeft, bottomRight)


if __name__ == '__main__':
    solution = Solution()

    t0_4 = Node(False, True, None, None, None, None)
    t0_3 = Node(False, True, None, None, None, None)
    t0_2 = Node(True, True, None, None, None, None)
    t0_1 = Node(True, True, None, None, None, None)
    t0_0 = Node(None, False, t0_1, t0_2, t0_3, t0_4)

    t1_8 = Node(True, True, None, None, None, None)
    t1_7 = Node(True, True, None, None, None, None)
    t1_6 = Node(False, True, None, None, None, None)
    t1_5 = Node(False, True, None, None, None, None)
    t1_4 = Node(False, True, None, None, None, None)
    t1_3 = Node(True, True, None, None, None, None)
    t1_2 = Node(None, False, t1_5, t1_6, t1_7, t1_8)
    t1_1 = Node(True, True, None, None, None, None)
    t1_0 = Node(None, False, t1_1, t1_2, t1_3, t1_4)

    t2_4 = Node(False, True, None, None, None, None)
    t2_3 = Node(True, True, None, None, None, None)
    t2_2 = Node(True, True, None, None, None, None)
    t2_1 = Node(True, True, None, None, None, None)
    t2_0 = Node(None, False, t2_1, t2_2, t2_3, t2_4)

    assert t2_0 == solution.intersect(t0_0, t1_0)
