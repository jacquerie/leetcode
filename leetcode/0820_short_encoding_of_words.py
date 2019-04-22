# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.leaf = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.leaf = True

    def minimumLengthEncoding(self):
        result = 0
        for child in self.root.children:
            result += self.depthOfLeaves(self.root.children[child], 1)
        return result

    def depthOfLeaves(self, current, length):
        if not current.children:
            return length + 1

        result = 0
        for child in current.children:
            result += self.depthOfLeaves(current.children[child], length + 1)
        return result


class Solution(object):
    def minimumLengthEncoding(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word[::-1])
        return trie.minimumLengthEncoding()


if __name__ == '__main__':
    solution = Solution()

    assert 10 == solution.minimumLengthEncoding(['time', 'me', 'bell'])
    assert 12 == solution.minimumLengthEncoding(['time', 'atime', 'btime'])
