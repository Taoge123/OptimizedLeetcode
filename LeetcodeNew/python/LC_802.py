

class Solution1:
    def eventualSafeNodes(self, graph):
        # color[i], 0 means not visited. 1 means safe. 2 means unsafe.
        table = [0] * len(graph)
        res = []
        for start in range(len(graph)):
            if self.dfs(graph, start, table):
                res.append(start)
        res.sort()
        return res

    def dfs(self, graph, start, table):
        # 返回start节点是否是安全，如果是，返回True
        if table[start] != 0:
            return table[start] == 1
        table[start] = 2
        for nei in graph[start]:
            if not self.dfs(graph, nei, table):
                return False
        table[start] = 1
        return True


