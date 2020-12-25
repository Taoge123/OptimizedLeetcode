
import collections

class Solution:
    def criticalConnections(self, n: int, connections):

        graph = collections.defaultdict(list)

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        table = [float('inf')] * n

        res = []

        def dfs(node, parent, step):
            table[node] = step
            for child in graph[node]:
                if child == parent:
                    continue
                elif table[child] == float('inf'):
                    table[node] = min(table[node], dfs(child, node, step + 1))
                else:
                    table[node] = min(table[node], table[child])
            if table[node] == step and parent != -1:
                res.append([parent, node])
            return table[node]

        dfs(0, -1, 0)
        return res


