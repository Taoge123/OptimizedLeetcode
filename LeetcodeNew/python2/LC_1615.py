import collections

class Solution:
    def maximalNetworkRank(self, n: int, roads) -> int:
        graph = collections.defaultdict(set)
        res = 0
        for x, y in roads:
            graph[x].add(y)
            graph[y].add(x)
        for i in range(n):
            for j in range(i + 1, n):
                count = len(graph[i]) + len(graph[j])
                # if both cities are connected, then we subtract 1
                if j in graph[i]:
                    count -= 1
                res = max(res, count)
        return res



