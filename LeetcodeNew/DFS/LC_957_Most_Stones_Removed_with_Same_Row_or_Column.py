"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/197668/Count-the-Number-of-Islands-O(N)
https://www.jianshu.com/p/30d2058db7f7
https://buptwc.com/2018/11/25/Leetcode-947-Most-Stones-Removed-with-Same-Row-or-Column/
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/198657/Python-DFS-Time-O(N)-Space-O(N)


Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0

"""

import collections


class DSU:
    def __init__(self, N):
        self.parent = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.parent[xr] = yr

class Solution(object):
    def removeStones(self, stones):
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})

class DFS1:
    def removeStones(self, points):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        for i, j in points:
            rows[i].add(j)
            cols[j].add(i)

        def dfsRow(i):
            seenR.add(i)
            for j in rows[i]:
                if j not in seenC:
                    dfsCol(j)

        def dfsCol(j):
            seenC.add(j)
            for i in cols[j]:
                if i not in seenR:
                    dfsRow(i)

        seenR, seenC = set(), set()
        islands = 0
        for i, j in points:
            if i not in seenR:
                islands += 1
                dfsRow(i)
                dfsCol(j)
        return len(points) - islands


class DFS2:
    def removeStones(self, points):
        index = collections.defaultdict(set)
        for i, j in points:
            index[i].add(j + 10000)
            index[j + 10000].add(i)

        def dfs(i):
            seen.add(i)
            for j in index[i]:
                if j not in seen:
                    dfs(j)

        seen = set()
        islands = 0
        for i, j in points:
            if i not in seen:
                islands += 1
                dfs(i)
                dfs(j + 10000)
        return len(points) - islands



class SolutionLee:
    def removeStones(self, points):
        UF = {}

        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)

        for i, j in points:
            union(i, ~j)
        return len(points) - len({find(x) for x in UF})




class Solution2(object):
    def removeStones(self, stones):
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        for i in range(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                ans -= 1
        return ans




