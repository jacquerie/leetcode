# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


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


class Codec(object):
    def serialize(self, root):
        if root is None:
            return '()'
        return ''.join([
            '(',
            str(root.val),
            self.serialize(root.left),
            self.serialize(root.right),
            ')',
        ])

    def deserialize(self, data):
        if len(data) == 2:
            return None

        i, val = self.parseVal(data)
        j = self.parseSubtree(data, i)

        node = TreeNode(val)
        node.left = self.deserialize(data[i:j])
        node.right = self.deserialize(data[j:-1])

        return node

    def parseVal(self, data):
        i = 1
        while data[i].isdigit() or data[i] == '-':
            i += 1
        return i, int(data[1:i])

    def parseSubtree(self, data, i):
        n = 1
        while n:
            i += 1
            if data[i] == '(':
                n += 1
            elif data[i] == ')':
                n -= 1
        return i + 1


if __name__ == '__main__':
    obj = Codec()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(3)
    t0_3 = TreeNode(4)
    t0_4 = TreeNode(5)
    t0_2.right = t0_4
    t0_2.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert '(1(2()())(3(4()())(5()())))' == obj.serialize(t0_0)
    assert t0_0 == obj.deserialize('(1(2()())(3(4()())(5()())))')

    t1_0 = TreeNode(-1)
    t1_1 = TreeNode(0)
    t1_2 = TreeNode(1)
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert '(-1(0()())(1()()))' == obj.serialize(t1_0)
    assert t1_0 == obj.deserialize('(-1(0()())(1()()))')
