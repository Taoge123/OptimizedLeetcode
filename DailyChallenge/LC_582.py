import collections

class Solution:
    def killProcess(self, pid, ppid, kill: int):
        graph = collections.defaultdict(list)
        for i, j in zip(ppid, pid):
            graph[i].append(j)

        res = []
        self.helper(graph, kill, res)
        return res

    def helper(self, graph, kill, res):
        res.append(kill)
        for i in graph[kill]:
            self.helper(graph, i, res)


