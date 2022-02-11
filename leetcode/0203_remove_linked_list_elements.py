# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return other is not None and self.val == other.val and self.next == other.next


class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(None)
        dummy.next = head

        previous, current = dummy, dummy.next
        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
            current = current.next

        return dummy.next


if __name__ == "__main__":
    solution = Solution()

    l0_0 = ListNode(1)
    l0_1 = ListNode(2)
    l0_2 = ListNode(6)
    l0_3 = ListNode(3)
    l0_4 = ListNode(4)
    l0_5 = ListNode(5)
    l0_6 = ListNode(6)
    l0_0.next = l0_1
    l0_1.next = l0_2
    l0_2.next = l0_3
    l0_3.next = l0_4
    l0_4.next = l0_5
    l0_5.next = l0_6

    l1_0 = ListNode(1)
    l1_1 = ListNode(2)
    l1_2 = ListNode(3)
    l1_3 = ListNode(4)
    l1_4 = ListNode(5)
    l1_0.next = l1_1
    l1_1.next = l1_2
    l1_2.next = l1_3
    l1_3.next = l1_4

    assert l1_0 == solution.removeElements(l0_0, 6)

    l2_0 = ListNode(1)
    l2_1 = ListNode(1)
    l2_0.next = l2_1

    assert solution.removeElements(l2_0, 1) is None
