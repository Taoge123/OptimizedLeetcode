class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True


class Solution:
    def indexPairs(self, text: str, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        res = []
        n = len(text)
        for i in range(n):
            j = i
            node = trie.root
            while j < n and text[j] in node.children:
                node = node.children[text[j]]
                if node.isWord:
                    res.append([i, j])
                j += 1
        return res




class Solution2:
    def indexPairs(self, text: str, words):
        res = []
        n = len(text)

        for i in range(n):
            for word in words:
                j = i + len(word) - 1
                if j< n and text[i:j + 1] == word:
                    res.append([i, j])
        res.sort()
        return res



