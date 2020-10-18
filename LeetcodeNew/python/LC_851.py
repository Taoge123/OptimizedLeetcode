class Solution:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for u, v in richer:
            graph[v].append(u)

        res = [0] * n
        for i in range(n):
            self.dfs(graph, i, quiet, res)
        return res

    def dfs(self, graph, node, quiet, res):
        # Want least quiet person in this subtree
        if res[node]:
            return res[node]
        res[node] = node
        for nei in graph[node]:
            cand = self.dfs(graph, nei, quiet, res)
            if quiet[cand] < quiet[res[node]]:
                res[node] = cand
        return res[node]



