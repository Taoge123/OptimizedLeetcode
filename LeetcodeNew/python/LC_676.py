
import collections


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}


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

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isWord


class MagicDictionaryTony:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, word: str) -> bool:
        self.modified = False
        return self.dfs(self.trie.root, 0, word)

    def dfs(self, node, i, word):
        if i == len(word):
            return node.isWord and self.modified

        if self.modified:
            if word[i] in node.children:
                return self.dfs(node.children[word[i]], i + 1, word)
            else:
                # 2 diffs, then return False
                return False
        else:
            for ch in node.children:
                # set mpdified if seeing first diff
                self.modified = ch != word[i]
                if self.dfs(node.children[ch], i + 1, word):
                    return True
            return False


class MagicDictionaryRika:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        node = self.trie.root
        return self.dfs(node, searchWord, 0, 1)

    def dfs(self, node, word, i, k):
        if k < 0:
            return False

        if i == len(word):
            return k == 0 and node.isWord

        ch = word[i]
        if ch in node.children:
            if self.dfs(node.children[ch], word, i + 1, k):
                return True

        for child in node.children:
            if ch != child and self.dfs(node.children[child], word, i + 1, k - 1):
                return True
        return False


class MagicDictionary:
    def __init__(self):
        self.table = collections.defaultdict(set)

    def buildDict(self, dictionary) -> None:
        for word in dictionary:
            n = len(word)
            if n not in self.table:
                self.table[n] = set()
            self.table[n].add(word)

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        if n not in self.table:
            return False

        for s in self.table[n]:
            count = 0
            for i in range(n):
                if searchWord[i] != s[i]:
                    count += 1

            if count == 1:
                return True

        return False



