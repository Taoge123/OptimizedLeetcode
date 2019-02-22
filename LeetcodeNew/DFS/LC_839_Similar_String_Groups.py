"""
We simply construct edges for every string in A but construction method differs for 2 cases as len(A[i]) * len(A) <= 20 000.

Case 1: For short length of A[i] and long length of A, we find every swaps in A[i].
Runtime: O(N(L^2) )
00
00
00
00

Case 2: For long length of A[i] and short length of A, we compare every A[i] and A[j] in A by checking characters instead of swap variations.
If they differ just by 2 characters theres is edge between them.
Runtime: O((N^2)L)
0000
0000

"""
import collections
import itertools


class DSU:
    def __init__(self, N):
        self.par = range(N)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

class Solution: # (NW) * min(N, W*W) complexity
    def numSimilarGroups(self, A):
        N, W = len(A), len(A[0])

        def similar(word1, word2):
            diff = 0
            for x, y in itertools.izip(word1, word2):
                if x != y:
                    diff += 1
            return diff <= 2

        dsu = DSU(N)

        if N < W*W: # If few words, then check for pairwise similarity: O(N^2 W)
            for (i1, word1), (i2, word2) in \
                    itertools.combinations(enumerate(A), 2):
                if similar(word1, word2):
                    dsu.union(i1, i2)

        else: # If short words, check all neighbors: O(N W^3)
            buckets = collections.defaultdict(set)
            for i, word in enumerate(A):
                L = list(word)
                for j0, j1 in itertools.combinations(range(W), 2):
                    L[j0], L[j1] = L[j1], L[j0]
                    buckets["".join(L)].add(i)
                    L[j0], L[j1] = L[j1], L[j0]

            for i1, word in enumerate(A):
                for i2 in buckets[word]:
                    dsu.union(i1, i2)

        return sum(dsu.par[x] == x for x in range(N))


def numSimilarGroups(self, A):
    parents = {x: x for x in A}
    n, m = len(A), len(A[0])
    self.count = n

    def find(x):
        if x != parents[x]: parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            parents[x] = y
            self.count -= 1
            return True
        return False

    def similar(x, y):
        return sum(i != j for i, j in zip(x, y)) == 2

    ## Real Solution Part ##
    if n < m:
        for x, y in itertools.combinations(A, 2):
            if similar(x, y): union(x, y)
    else:
        for x in A:
            for i, j in itertools.combinations(range(m), 2):
                y = x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:]
                if y in parents: union(x, y)
    return self.count

class Solution2:
    def are_similar(self, word1, word2):
        mismatches = 0

        for i in range(len(word1)):
            if word1[i] != word2[i]:
                mismatches += 1
                if mismatches > 2:
                    return False

        return True

    def dfs(self, A, i, visited, adj_list):
        visited[i] = True

        for next_word_idx in adj_list[i]:
            if not visited[next_word_idx]:
                self.dfs(A, next_word_idx, visited, adj_list)

    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        adj_list = collections.defaultdict(list)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if self.are_similar(A[i], A[j]):
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        visited = [False] * len(A)
        group_cnt = 0
        for i in range(len(A)):
            if not visited[i]:
                self.dfs(A, i, visited, adj_list)
                group_cnt += 1

        return group_cnt

