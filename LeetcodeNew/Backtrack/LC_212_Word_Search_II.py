import collections

class Solution:
    def findWords(self, board, words):
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board, i, j, trie, '', res)
        return list(set(res))

    def find(self, board, i, j, trie, path, res):
        if '#' in trie:
            res.append(path)
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] not in trie:
            return
        tmp = board[i][j]
        board[i][j] ="@"
        self.find(board, i+1, j, trie[tmp], path+tmp, res)
        self.find(board, i, j+1, trie[tmp], path+tmp, res)
        self.find(board, i-1, j, trie[tmp], path+tmp, res)
        self.find(board, i, j-1, trie[tmp], path+tmp, res)
        board[i][j] = tmp


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in xrange(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp



