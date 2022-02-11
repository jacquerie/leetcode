# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return other is not None and self.val == other.val and self.next == other.next


class Solution:
    def middleNode(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    solution = Solution()

    l0_0 = ListNode(1)
    l0_1 = ListNode(2)
    l0_2 = ListNode(3)
    l0_3 = ListNode(4)
    l0_4 = ListNode(5)
    l0_3.next = l0_4
    l0_2.next = l0_3
    l0_1.next = l0_2
    l0_0.next = l0_1

    l1_0 = ListNode(3)
    l1_1 = ListNode(4)
    l1_2 = ListNode(5)
    l1_1.next = l1_2
    l1_0.next = l1_1

    assert l1_0 == solution.middleNode(l0_0)
