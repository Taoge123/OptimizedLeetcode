

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class SolutionRika:
    def countDistinct(self, s: str) -> int:
        n = len(s)
        base = 26
        mod = 2 ** 63 - 1

        seen = set()
        for i in range(n):
            hashcode = 1  # 初始值必须为1，因为如果为0的话，a和aa和aaa的hashcode是一样的
            for j in range(i, n):
                num = ord(s[j]) - ord("a")
                hashcode = (hashcode * base + num) % mod
                seen.add(hashcode)
        return len(seen)



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

                if newTrie.is_word == False:
                    newTrie.is_word = True
                    res += 1

        return res



class SolutionSet:
    def countDistinct(self, s: str) -> int:
        visited = set()
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                visited.add(s[i:j])
        return len(visited)


s = "aabbaba"
a = Solution()
print(a.countDistinct(s))