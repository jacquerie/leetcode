# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import deque


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.leaf = False
        self.value = None


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, value):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.leaf = True
        current.value = value

    def sum(self, prefix):
        node = self._walk(prefix)
        if node is None:
            return 0

        result = 0

        queue = deque([node])
        while queue:
            node = queue.popleft()
            if node.leaf:
                result += node.value
            for child in node.children:
                queue.append(node.children[child])

        return result

    def _walk(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
        return current


class MapSum(object):
    def __init__(self):
        self.trie = Trie()

    def insert(self, key, val):
        self.trie.insert(key, val)

    def sum(self, prefix):
        return self.trie.sum(prefix)


if __name__ == '__main__':
    obj = MapSum()

    obj.insert('apple', 3)
    assert 3 == obj.sum('ap')
    obj.insert('app', 2)
    assert 5 == obj.sum('ap')
