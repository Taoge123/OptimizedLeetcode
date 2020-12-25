
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class SolutionSet:
    def countDistinct(self, s: str) -> int:
        visited = set()
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                visited.add(s[i:j])
        return len(visited)




class Solution:
    def countDistinct(self, s: str) -> int:

        trie = TrieNode()
        res = 0

        for i in range(len(s)):
            newTrie = trie
            for j in range(i, len(s)):
                ch = s[j]
                if ch not in newTrie.children:
                    newTrie.children[ch] = TrieNode()
                newTrie = newTrie.children[ch]

                if newTrie.isEnd == False:
                    newTrie.isEnd = True
                    res += 1

        return res



