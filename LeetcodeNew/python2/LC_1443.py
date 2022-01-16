"""
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/discuss/772044/Python-O(n)-by-DFS-w-Visualization
"""

import collections

class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        return self.dfs(graph, hasApple, 0, visited)

    def dfs(self, graph, hasApple, node, visited):
        visited.add(node)
        res = 0

        for nei in graph[node]:
            if nei in visited:
                continue

            cost = self.dfs(graph, hasApple, nei, visited)

            if cost or hasApple[nei]:
                # update cost of collection (i.e., cost of green arrows)
                # The first +1 is for path from cur_node to child_node, and the second +1 is for going back.
                # Totally, +2
                res += cost + 2

        return res


