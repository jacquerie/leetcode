# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return other is not None and self.val == other.val and self.next == other.next


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    solution = Solution()

    l0_0 = ListNode(1)
    l0_1 = ListNode(2)
    l0_2 = ListNode(3)
    l0_3 = ListNode(4)
    l0_0.next = l0_1
    l0_1.next = l0_2
    l0_2.next = l0_3

    l1_0 = ListNode(1)
    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_0.next = l1_1
    l1_1.next = l1_2

    assert solution.deleteNode(l0_2) is None
    assert l0_0 == l1_0
