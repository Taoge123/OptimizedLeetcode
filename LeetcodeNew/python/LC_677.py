
import collections


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.count = 0


class MapSumTony:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children.get(char)
        node.count = val
        node.isWord = True

    def sum(self, prefix: str) -> int:
        node = self.root
        self.res = 0
        for char in prefix:
            node = node.children.get(char)
            if not node:
                return 0

        self.dfs(node)
        return self.res

    def dfs(self, node):
        self.res += node.count
        for child in node.children.keys():
            # print(type(child))
            self.dfs(node.children[child])


class MapSum:
    def __init__(self):
        self.table = collections.defaultdict(int)
        self.words = collections.defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        diff = val - self.table[key]
        self.table[key] = val
        prefix = ""
        for c in key:
            prefix += c
            self.words[prefix] = self.words[prefix] + diff

    def sum(self, prefix: str) -> int:
        return self.words[prefix]




