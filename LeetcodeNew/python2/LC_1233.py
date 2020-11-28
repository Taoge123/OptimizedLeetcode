
"""
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/409075/Standard-Python-Trie-solution-(similar-problems-listed)
208. Implement Trie (Prefix Tree)
211. Add and Search Word - Data structure design
425. Word Squares
676. Implement Magic Dictionary
677. Map Sum Pairs
745. Prefix and Suffix Search
1032. Stream of Characters
1233. Remove Sub-Folders from the Filesystem

"""



class Solution2:
    def removeSubfolders(self, folder):
        A = set(folder)
        for f in folder:
            for i, char in enumerate(f):
                if char == '/':
                    root = f[:i]
                    if root in A:
                        A.remove(f)
                        break

        return list(A)



class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def find(self):
        res = []
        self.dfs(self.root, [], res)
        return res

    def dfs(self, node, path, res):
        if node.isEnd:
            res.append('/' + '/'.join(path))
            # 加完第一层提前return， 遇到相同的prefix就不会重新加了
            return
        for char in node.children:
            self.dfs(node.children[char], path + [char], res)


class Solution:
    def removeSubfolders(self, folder):
        trie = Trie()
        for f in folder:
            f = f.split('/')[1:]
            trie.insert(f)
        return trie.find()



folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
a = Solution2()
print(a.removeSubfolders(folder))
