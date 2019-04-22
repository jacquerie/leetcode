# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Iterator(object):
    def __init__(self, nums):
        self.nums = nums

    def hasNext(self):
        return bool(self.nums)

    def next(self):
        return self.nums.pop()


class PeekingIterator(object):
    def __init__(self, iterator):
        self.cache = None
        self.iterator = iterator

    def peek(self):
        if self.cache is None:
            self.cache = self.iterator.next()
        return self.cache

    def hasNext(self):
        if self.cache is not None:
            return True
        return self.iterator.hasNext()

    def next(self):
        if self.cache is not None:
            result = self.cache
            self.cache = None
            return result
        return self.iterator.next()


if __name__ == '__main__':
    iterator = PeekingIterator(Iterator([1, 2, 3]))
    assert iterator.hasNext()
    assert 3 == iterator.peek()
    assert 3 == iterator.next()
