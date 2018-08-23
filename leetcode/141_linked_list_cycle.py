# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return (
            other is not None and
            self.val == other.val and
            self.next == other.next
        )


class Solution(object):
    def hasCycle(self, head):
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if id(slow) == id(fast):
                return True
        return False


if __name__ == '__main__':
    solution = Solution()

    l0_0 = ListNode(1)
    l0_1 = ListNode(2)
    l0_2 = ListNode(3)
    l0_3 = ListNode(4)
    l0_4 = ListNode(5)
    l0_4.next = l0_3
    l0_3.next = l0_4
    l0_2.next = l0_3
    l0_1.next = l0_2
    l0_0.next = l0_1

    assert solution.hasCycle(l0_0)
