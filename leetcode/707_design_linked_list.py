# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList(object):
    def __init__(self):
        self.count = 0
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        node = self._traverse(index)
        if node is not None:
            return node.val
        return -1

    def addAtHead(self, val):
        self._add(self.head, val)

    def addAtTail(self, val):
        self._add(self.tail.prev, val)

    def addAtIndex(self, index, val):
        prev = self._traverse(index - 1)
        if prev is not None:
            self._add(prev, val)

    def deleteAtIndex(self, index):
        node = self._traverse(index)
        if node is not None:
            self._delete(node)

    def _add(self, prev, val):
        self.count += 1
        node = ListNode(val)
        node.next = prev.next
        node.next.prev = node
        prev.next = node
        prev.next.prev = prev

    def _delete(self, node):
        self.count -= 1
        node.prev.next = node.next
        node.next.prev = node.prev

    def _traverse(self, index):
        if -1 <= index < self.count // 2:
            return self._traverse_forward(index)
        elif self.count // 2 <= index < self.count:
            return self._traverse_backward(index)
        return None

    def _traverse_forward(self, index):
        current, current_index = self.head, -1
        while current_index < index:
            current, current_index = current.next, current_index + 1
        return current

    def _traverse_backward(self, index):
        current, current_index = self.tail, self.count
        while current_index > index:
            current, current_index = current.prev, current_index - 1
        return current


if __name__ == '__main__':
    obj = MyLinkedList()

    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    assert 2 == obj.get(1)
    obj.deleteAtIndex(1)
    assert 3 == obj.get(1)

    obj = MyLinkedList()

    obj.addAtHead(1)
    obj.addAtIndex(1, 2)
    assert 1 == obj.get(0)
    assert -1 == obj.get(2)

    obj = MyLinkedList()

    assert -1 == obj.get(0)
    obj.addAtIndex(1, 2)
    assert -1 == obj.get(0)
    assert -1 == obj.get(1)
    obj.addAtIndex(0, 1)
    assert 1 == obj.get(0)
    assert -1 == obj.get(1)
