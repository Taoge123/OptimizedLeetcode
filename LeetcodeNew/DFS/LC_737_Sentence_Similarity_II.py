"""
The specific algorithm we go for is an iterative depth-first search.
The implementation we go for is a typical "visitor pattern":
when searching whether there is a path from w1 = words1[i] to w2 = words2[i],
stack will contain all the nodes that are queued up for processing,
while seen will be all the nodes that have been queued for processing
(whether they have been processed or not).
"""
import collections
import itertools

class Solution1:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2): return False
        graph = collections.defaultdict(list)
        for w1, w2 in pairs:
            graph[w1].append(w2)
            graph[w2].append(w1)

        for w1, w2 in zip(words1, words2):
            stack, seen = [w1], {w1}
            while stack:
                word = stack.pop()
                if word == w2: break
                for nei in graph[word]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            else:
                return False
        return True


"""
Algorithm

Draw edges between words if they are similar. 
For easier interoperability between our DSU template, 
we will map each word to some integer ix = index[word]. 
Then, dsu.find(ix) will tell us a unique id representing what component that word is in.

For more information on DSU, please look at Approach #2 in the article here. 
For brevity, the solutions showcased below do not use union-by-rank.

After putting each word in pairs into our DSU template, 
we check successive pairs of words w1, w2 = words1[i], words2[i]. 
We require that w1 == w2, or w1 and w2 are in the same component. 
This is easily checked using dsu.find.
"""


class DSU:
    def __init__(self, N):
        self.par = range(N)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

class Solution2:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2): return False

        index = {}
        count = itertools.count()
        dsu = DSU(2 * len(pairs))
        for pair in pairs:
            for p in pair:
                if p not in index:
                    index[p] = next(count)
            dsu.union(index[pair[0]], index[pair[1]])

        return all(w1 == w2 or
                   w1 in index and w2 in index and
                   dsu.find(index[w1]) == dsu.find(index[w2])
                   for w1, w2 in zip(words1, words2))


class Solution3:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False
        similar = collections.defaultdict(dict)

        for words in pairs:
            for word1 in words:
                for word2 in words:
                    similar[word1][word2] = True
                    similar[word2][word1] = True

        for k in similar:
            for i in similar[k]:
                for j in similar[k]:
                    similar[i][j] = True
                    similar[j][i] = True

        for w1, w2 in zip(words1, words2):

            if len(similar.get(w1, {})) == 0 and w1 != w2:
                return False
            if not similar[w1].get(w2, False) and w1 != w2:
                return False
        return True


class DSU:  # DSU 类适用于所有union find 的问题
    def __init__(self, n):  # n 选一个足够大的数即可。
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        self.parent[p_x] = p_y


class Solution4:
    def areSentencesSimilarTwo(self, words1, words2, pairs):

        if len(words1) != len(words2):
            return False
        i = 0  # 每个word的id
        word2id = {}  # word -> ID

        dsu = DSU(2 * len(pairs))  # 大小下限是 unique word in pairs， 没有上限，可以选择任意大的数

        for w1, w2 in pairs:
            if w1 not in word2id:  # 建立映射
                word2id[w1] = i
                i += 1
            if w2 not in word2id:
                word2id[w2] = i
                i += 1
            dsu.merge(word2id[w1], word2id[w2])  # 两个word在同一个pair里，把两个id merge即可

        for w1, w2 in zip(words1, words2):
            if w1 == w2:  # Corner case: 单词本身跟自己相似，不管他们在不在pairs 表里。
                continue
            if not w1 in word2id or not w2 in word2id:  # Corner case: words1 和words2里的单词可能不在pairs 表里，表示他们不可能跟其他单词有相似关系。
                return False
            if dsu.find(word2id[w1]) != dsu.find(word2id[w2]):  # 只要判断两个单词的id 是否指向共同的parent
                return False
        return True

