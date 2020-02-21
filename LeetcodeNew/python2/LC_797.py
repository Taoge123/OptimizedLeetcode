class SolutionLee:
    def allPathsSourceTarget(self, graph):
        res = []
        self.dfs(graph, 0, [0], res)
        return res

    def dfs(self, graph, i, path, res):
        if i == len(graph) - 1:
            res.append(path)
            return

        for nei in graph[i]:
            self.dfs(graph, nei, path + [nei], res)


class Solution2:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        return self.dfs(graph, 0, n)

    def dfs(self, graph, node, n):
        if node == n - 1:
            return [[n - 1]]
        res = []
        for nei in graph[node]:
            for path in self.dfs(graph, nei, n):
                res.append([node] + path)
        return res






