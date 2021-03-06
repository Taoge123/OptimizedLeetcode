"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]


Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.

"""


import collections

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        res = []
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)

        for i in range(m):
            for j in range(n):
                self.dfs(board, node,  i, j, m, n, "", res)
        return res

    def dfs(self, board, node, i, j, m, n, path, res):

        if node.isWord:
            res.append(path)
            node.isWord = False

        if i< 0 or j < 0 or i >= m or j >= n:
            return
        node = node.children.get(board[i][j])
        if not node:
            return
        temp = board[i][j]
        board[i][j] = "#"
        self.dfs(board, node, i - 1, j, m, n, path + temp, res)
        self.dfs(board, node, i + 1, j, m, n, path + temp, res)
        self.dfs(board, node, i, j - 1, m, n, path + temp, res)
        self.dfs(board, node, i, j + 1, m, n, path + temp, res)
        board[i][j] = temp




board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

a = Solution()
print(a.findWords(board, words))


