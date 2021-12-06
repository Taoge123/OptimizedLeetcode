
"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""

import collections


class Solution:
    def validTree(self, n: int, edges) -> bool:
        graph = collections.defaultdict(list)
        visited = collections.defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return not self.hasCycle(graph, visited, 0, -1) and n == len(visited)

    def hasCycle(self, graph, visited, node, parent):
        visited[node] = -1
        for nei in graph[node]:
            if nei != parent:
                if visited[nei] == -1 or self.hasCycle(graph, visited, nei, node):
                    return True
        return False


class Solution2:
    def validTree(self, n: int, edges) -> bool:
        nums = [-1] * n
        for u, v in edges:
            if not self.union(nums, u, v):
                return False
        return len(edges) == n - 1


    def find(self, nums, i):
        if nums[i] == -1:
            return i
        return self.find(nums, nums[i])

    def union(self, nums, i, j):
        x = self.find(nums, i)
        y = self.find(nums, j)
        if x == y:
            return False
        else:
            nums[x] = y
            return True









