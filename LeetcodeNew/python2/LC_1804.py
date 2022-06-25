
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.prefix_count = 0
        self.tail_count = 0
        self.count = 0

class TrieTony:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if not node:
                return 0
        return node.count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if not node:
                return 0
        self.res = 0
        self.dfs(node)
        return self.res

    def dfs(self, node):
        if not node:
            return
        if not node.children:
            self.res += node.count
            return
        self.res += node.count
        for ch in node.children:
            self.dfs(node.children[ch])
        return self.res

    def erase(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return
            node = node.children[ch]
        node.count -= 1


class TrieRika:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.prefix_count += 1

        node.isWord = True
        node.tail_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if not node:
                return 0
        return node.tail_count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if not node:
                return 0
        return node.prefix_count

    def erase(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            node.prefix_count -= 1
        node.tail_count -= 1

    # Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)

