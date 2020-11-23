
class Solution:
    def isBipartite(self, graph) -> bool:
        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not self.dfs(graph, color, i):
                    return False

        return True

    def dfs(self, graph, color, pos):
        for i in graph[pos]:
            if i in color:
                if color[i] == color[pos]:
                    return False
            else:
                color[i] = 1 - color[pos]
                if not self.dfs(graph, color, i):
                    return False

        return True


