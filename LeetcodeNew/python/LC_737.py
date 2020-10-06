

import collections


class Solution:
    def find(self, w, parent):
        if parent[w] == w:
            return parent[w]
        return self.find(parent[w], parent)

    def union(self, i, j, parent):
        x = self.find(i, parent)
        y = self.find(j, parent)
        parent[x] = y

    def areSentencesSimilarTwo(self, words1, words2, pairs):
        parent = collections.defaultdict(str)
        for word in words1 + words2:
            parent[word] = word

        for i, j in pairs:
            self.union(i, j, parent)

        n1, n2 = len(words1), len(words2)
        if n1 != n2:
            return False

        for i in range(n1):
            x = self.find(words1[i], parent)
            y = self.find(words2[i], parent)
            if x != y:
                return False
        return True



class SolutionDFS:
    def dfs(self, word, root_word, roots, connections):
        # print(word, root_word)
        if word in roots: return None
        roots[word] = root_word
        for connectedWord in connections[word]:
            self.dfs(connectedWord, root_word, roots, connections)


    def areSentencesSimilarTwo(self,words1,words2,pairs):
        if len(words1)!=len(words2):
            return False

        connections = collections.defaultdict(set)
        #build the graph
        for w1,w2 in pairs:
            connections[w1].add(w2)
            connections[w2].add(w1)

        roots = {}
        for word in connections:
            self.dfs(word,word,roots, connections)

        for w1,w2 in zip(words1,words2):
            if roots.get(w1,w1) != roots.get(w2,w2):
                return False
        return True



words1 = ["great", "acting", "skills"]
words2 = ["fine", "drama", "talent"]
pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]


a = Solution()
print(a.areSentencesSimilarTwo(words1,words2,pairs))


