
# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         graph = collections.defaultdict(list)
#         visited = set()
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)

#         return not self.dfs(graph, visited, 0, -1) and n == len(visited)


#     def dfs(self, graph, visited, node, parent):
#         visited.add(node)
#         for i in graph[node]:
#             if i != parent:
#                 if i in visited or self.dfs(graph, visited, i, node):
#                     return True
#         return False




class Solution:
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
        x, y = self.find(nums, i), self.find(nums, j)
        if x == y:
            return False
        else:
            nums[x] = y
            return True









