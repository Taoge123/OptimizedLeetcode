
"""
Similir with 332

https://leetcode.com/problems/reconstruct-itinerary/
https://github.com/wisdompeak/LeetCode/tree/master/Graph/2097.Valid-Arrangement-of-Pairs
https://www.youtube.com/watch?v=vRZcrOytvgs&t=161s


Euler path

欧拉路径

1.无向图：(a) 如果只有两个点的度是奇数，其他的点的度都是偶数，则存在从一个奇数度点到另一个奇数度点的欧拉路径（不是回路）。
         (b) 如果所有的点的度都是偶数，那么就是欧拉回路。

2.有向图：(a) 如果最多有一个点出度大于入度by1，且最多有一个点入度大于出度by1，那么就有一条从前者（如果没有则可以任意）到后者（如果没有则可以任意）的欧拉路径。
         (b) 如果所有的点的入度等于出度，那么就存在欧拉回路。

"""


import collections

class Solution:
    def validArrangement(self, pairs):

        in_degree = collections.defaultdict(int)
        out_degree = collections.defaultdict(int)
        self.graph = collections.defaultdict(list)

        for u, v in pairs:
            in_degree[v] += 1
            out_degree[u] += 1
            self.graph[u].append(v)

        start = -1
        for node in self.graph:
            if out_degree[node] - in_degree[node] == 1:
                start = node

        if start == -1:
            start = pairs[0][0]

        def dfs(node, path):
            while self.graph[node]:
                nei = self.graph[node].pop()
                dfs(nei, path)
            path.append(node)

        path = []
        dfs(start, path)
        res = []
        path = path[::-1]
        for i in range(len(path) - 1):
            res.append([path[i], path[i + 1]])

        return res





