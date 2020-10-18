
class Solution:
    def sumOfDistancesInTree(self, N: int, edges):
        self.tree = []
        res = [0] * N
        count = [0] * N

        for i in range(N):
            self.tree.append([])

        for u, v in edges:
            self.tree[u].append(v)
            self.tree[v].append(u)

        self.dfs(0, -1, count, res)
        self.dfs2(0, -1, count, res)

        return res

    def dfs(self, root, parent, count, res):
        for child in self.tree[root]:
            if child == parent:
                continue
            self.dfs(child, root, count, res)
            count[root] += count[child]
            res[root] += res[child] + count[child]
        count[root] += 1

    def dfs2(self, root, parent, count, res):
        for child in self.tree[root]:
            if child == parent:
                continue
            res[child] = res[root] - count[child] + len(count) - count[child]
            self.dfs2(child, root, count, res)



