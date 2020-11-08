import collections

class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        graph = collections.defaultdict(list)
        res = [0] * n
        visited = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        self.dfs(graph, labels, 0, visited, res)
        return res

    def dfs(self, graph, labels, node, visited, res):
        count = collections.Counter()
        if node not in visited:
            count[labels[node]] += 1
            visited.add(node)
            for child in graph[node]:
                count += self.dfs(graph, labels, child, visited, res)
            res[node] = count[labels[node]]
        return count


