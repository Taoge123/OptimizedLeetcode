
import collections


class Solution:
    def deleteTreeNodes(self, nodes: int, parent, value):
        graph = collections.defaultdict(list)
        for i in range(nodes):
            graph[parent[i]].append(i)
        x, y = self.dfs(graph, value, 0)
        return y

    def dfs(self, graph, value, node):
        summ = value[node]
        count = 1
        for nei in graph[node]:
            t, c = self.dfs(graph, value, nei)
            summ += t
            count += c

        if summ == 0:
            return 0, 0

        return summ, count



