
import collections

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



class SolutionDFS:
    def eventualSafeNodes(self, graph):
        res = []
        if not graph:
            return res

        color = [0] * len(graph)
        for i in range(len(graph)):
            if self.helper(graph, i, color):
                res.append(i)
        return res

    def helper(self, graph, cur, color):
        if color[cur] != 0:
            return color[cur] == 2

        color[cur] = 1
        for nei in graph[cur]:
            if not self.helper(graph, nei, color):
                return False
        color[cur] = 2
        return True



class SolutionBFS:
    def eventualSafeNodes(self, graph):
        res = []
        if not graph:
            return res

        degree = [0] * len(graph)
        table = collections.defaultdict(set)

        for i in range(len(graph)):
            for nei in graph[i]:
                table[nei].add(i)
                degree[i] += 1

        res = set()
        queue = collections.deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                res.add(i)
                queue.append(i)

        while queue:
            node = queue.popleft()
            res.add(node)
            if node in table:
                for nei in table[node]:
                    degree[nei] -= 1
                    if degree[nei] == 0:
                        queue.append(nei)

        return sorted(list(res))



