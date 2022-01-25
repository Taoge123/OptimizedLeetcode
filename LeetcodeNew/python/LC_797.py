
class SolutionTony:
    def allPathsSourceTarget(self, graph):

        res = []
        n = len(graph)

        def dfs(node, target, path, res):
            if node == target:
                res.append(path + [target])

            for nei in graph[node]:
                dfs(nei, target, path + [node], res)

        dfs(0, n - 1, [], res)
        return res



class SolutionLee:
    def allPathsSourceTarget(self, graph):
        res = []
        self.dfs(graph, 0, [0], res)
        return res

    def dfs(self, graph, node, path, res):
        if node == len(graph) - 1:
            res.append(path)
            return

        for nei in graph[node]:
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






