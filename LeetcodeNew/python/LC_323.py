
"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

import collections


class Solution:
    def countComponents(self, n: int, edges) -> int:
        result = n
        nums = [-1] * n
        for u, v in edges:
            if self.union(nums, u, v):
                result -= 1
        return result

    def find(self, nums, i):
        if nums[i] == -1:
            return i
        return self.find(nums, nums[i])

    def union(self, nums, i, j):
        x, y = self.find(nums, i), self.find(nums, j)
        if x == y:
            return False
        nums[x] = y
        return True


class Solution:
    def countComponents(self, n: int, edges) -> int:
        result = n
        nums = [i for i in range(n)]

        for edge in edges:
            if self.unite(edge[0], edge[1], nums):
                result -= 1

        return result


    def find(self, nums, i):
        while nums[i] != i: # 假如不相同，意味着start已经被归入了集合
            nums[i] = nums[nums[i]] # 往下深入，寻找最终的id
            i = nums[i] #
        return i

    def unite(self, i, j, nums):
        x, y = self.find(nums, i), self.find(nums, j)
        if x == y: # 同一个集合
            return False
        else: # 不同id，连接成一个集合
            nums[x] = y
            return True


class Solution:
    def countComponents(self, n, edges):
        graph = collections.defaultdict(list)
        visited = set()
        res = 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for i in range(n):
            if self.dfs(graph, i, visited):
                res += 1
        return res

    def dfs(self, graph, node, visited):

        if node in visited:
            return False
        visited.add(node)
        for i in graph[node]:
            self.dfs(graph, i, visited)

        return True











