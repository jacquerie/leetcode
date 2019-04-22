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


class Solution(object):
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()

        visited = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.startingHere(board, trie, visited, result, trie.root, '', i, j)

        return list(result)

    def startingHere(self, board, trie, visited, result, current_node, current_word, i, j):
        if current_node.leaf:
            result.add(current_word)

        out_of_bounds = i < 0 or i >= len(board) or j < 0 or j >= len(board[0])
        if out_of_bounds:
            return

        already_visited = (i, j) in visited
        dead_end = board[i][j] not in current_node.children
        if already_visited or dead_end:
            return

        current_node = current_node.children[board[i][j]]
        current_word = current_word + board[i][j]

        visited.add((i, j))
        self.startingHere(board, trie, visited, result, current_node, current_word, i - 1, j)
        self.startingHere(board, trie, visited, result, current_node, current_word, i, j - 1)
        self.startingHere(board, trie, visited, result, current_node, current_word, i + 1, j)
        self.startingHere(board, trie, visited, result, current_node, current_word, i, j + 1)
        visited.remove((i, j))


if __name__ == '__main__':
    solution = Solution()

    expected = ['eat', 'oath']
    result = solution.findWords([
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v'],
    ], ['oath', 'pea', 'eat', 'rain'])

    assert sorted(expected) == sorted(result)
