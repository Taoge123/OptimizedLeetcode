import collections

class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1

        visited = set()
        graph = collections.defaultdict(list)

        count = 0
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei in visited:
                    continue
                dfs(nei)

        for node in range(n):
            if node in visited:
                continue
            dfs(node)
            count += 1
        return count - 1




class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)

        if x == y:
            return

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        elif self.rank[y] > self.rank[x]:
            x, y = y, x

        self.parent[y] = x

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]


class Solution:
    def makeConnected(self, n: int, connections) -> int:
        if len(connections) < n - 1:
            return -1

        uf = UnionFind()

        for num in range(n):
            uf.parent[num] = num
            uf.rank[num] = 1

        for i, j in connections:
            uf.union(i, j)

        return sum(uf.find(num) == num for num in range(n)) - 1




