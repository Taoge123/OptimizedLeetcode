class TreeNode:
    def __init__(self):
        self.children = {}
        self.data = None
        self.freq = 0

class Trie:
    def __init__(self):
        self.root = TreeNode()

    def add(self, word, freq):
        node = self.root

        for w in word:
            if w not in node.children:
                node.children[w] = TreeNode()
            node = node.children[w]

        node.freq = freq
        node.data = word

    def search(self, char, node=None):
        node = node or self.root
        if char not in node.children:
            return [], None

        res = self.dfs(node)
        return [i[1] for i in sorted(res)][:3], node.children[char]

    def dfs(self, node):
        res = []
        if node.data:
            res.append([-node.freq, node.data])
        for subnode in node.children.values():
            res.extend(self.dfs(subnode))
        return res

class GoogleSuggestion:
    def __init__(self, sentences, times):
        self.trie = Trie()
        self.node = self.trie.root
        self.word = ''

        for s, t in zip(sentences, times):
            self.trie.add(s, t)

    def input(self, c):
        if c == '#':
            self.trie.add(self.word, 1)
            self.word = ''
            self.node = self.trie.root
            return []
        self.word += c
        res, self.node = self.trie.search(c, self.node)
        return res


a = GoogleSuggestion(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
# 642 leetcode