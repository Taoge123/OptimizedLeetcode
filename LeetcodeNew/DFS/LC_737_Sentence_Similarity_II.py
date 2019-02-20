"""
The specific algorithm we go for is an iterative depth-first search.
The implementation we go for is a typical "visitor pattern":
when searching whether there is a path from w1 = words1[i] to w2 = words2[i],
stack will contain all the nodes that are queued up for processing,
while seen will be all the nodes that have been queued for processing
(whether they have been processed or not).
"""


# union find set
class SolutionUF:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        # construct union find set
        self.parents = {}
        for pair in pairs:
            if pair[0] not in self.parents:
                self.parents[pair[0]] = pair[0]
            if pair[1] not in self.parents:
                self.parents[pair[1]] = pair[1]
        for pair in pairs:
            self.union(pair[0], pair[1])

        # perform union find
        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            elif words1[i] not in self.parents or words2[i] not in self.parents:
                return False
            elif self.find(words1[i]) != self.find(words2[i]):
                return False
        return True

    def find(self, word):
        if self.parents[word] != word:
            p = self.find(self.parents[self.parents[word]])
            self.parents[word] = p
        return self.parents[word]

    def union(self, w1, w2):
        p1 = self.find(w1)
        p2 = self.find(w2)
        if p1 != p2:
            self.parents[p2] = p1


# based on the above solution, add union by rank
class SolutionUFRank:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        # construct union find set
        self.parents = {}
        self.rank = {}
        for pair in pairs:
            if pair[0] not in self.parents:
                self.parents[pair[0]] = pair[0]
                self.rank[pair[0]] = 0
            if pair[1] not in self.parents:
                self.parents[pair[1]] = pair[1]
                self.rank[pair[1]] = 0
        for pair in pairs:
            self.union(pair[0], pair[1])

        # perform union find
        for i in xrange(len(words1)):
            if words1[i] == words2[i]:
                continue
            elif words1[i] not in self.parents or words2[i] not in self.parents:
                return False
            elif self.find(words1[i]) != self.find(words2[i]):
                return False
        return True

    def find(self, word):
        if self.parents[word] != word:
            p = self.find(self.parents[self.parents[word]])
            self.parents[word] = p
        return self.parents[word]

    def union(self, w1, w2):
        p1 = self.find(w1)
        p2 = self.find(w2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parents[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parents[p1] = p2
            else:
                self.parents[p2] = p1
                self.rank[p1] += 1











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



class Solution5:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False
        similars = collections.defaultdict(set)
        for w1, w2 in pairs:
            similars[w1].add(w2)
            similars[w2].add(w1)

        def dfs(words1, words2, visits):
            for similar in similars[words2]:
                if words1 == similar:
                    return True
                elif similar not in visits:
                    visits.add(similar)
                    if dfs(words1, similar, visits):
                        return True
            return False

        for w1, w2 in zip(words1, words2):
            if w1 != w2 and not dfs(w1, w2, set([w2])):
                return False
        return True

"""
http://www.cnblogs.com/grandyang/p/8053934.html

这道题是之前那道Sentence Similarity的拓展，那道题说单词之间不可传递，
于是乎这道题就变成可以传递了，那么难度就增加了。不过没有关系，还是用我们的经典老三样来解，
BFS，DFS，和Union Find。我们先来看BFS的解法，其实这道题的本质是无向连通图的问题，
那么首先要做的就是建立这个连通图的数据结构，对于每个结点来说，我们要记录所有和其相连的结点，
所以我们建立每个结点和其所有相连结点集合之间的映射，
比如对于这三个相似对(a, b), (b, c)，和(c, d)，我们有如下的映射关系：

a -> {b}

b -> {a, c}

c -> {b, d}

d -> {c}

那么如果我们要验证a和d是否相似，就需要用到传递关系，a只能找到b，b可以找到a，c，为了不陷入死循环，
我们将访问过的结点加入一个集合visited，那么此时b只能去，c只能去d，那么说明a和d是相似的了。
那么我们用for循环来比较对应位置上的两个单词，如果二者相同，那么直接跳过去比较接下来的。
否则就建一个访问即可visited，建一个队列queue，然后把words1中的单词放入queue，
建一个布尔型变量succ，标记是否找到，然后就是传统的BFS遍历的写法了，从队列中取元素，
如果和其相连的结点中有words2中的对应单词，标记succ为true，并break掉。
否则就将取出的结点加入队列queue，并且遍历其所有相连结点，
将其中未访问过的结点加入队列queue继续循环
"""






