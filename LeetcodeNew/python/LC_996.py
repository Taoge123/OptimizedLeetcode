"""
https://www.youtube.com/watch?v=V5eeRgQsr6o
"""
import math
import collections

class Solution:
    def numSquarefulPerms(self, A) -> int:
        if len(A) <= 1:
            return 0

        visited = [False] * len(A)
        res = []
        A = sorted(A)
        self.dfs(A, visited, [], res)
        return len(res)

    def dfs(self, nums, visited, path, res):
        if len(path) == len(nums):
            res.append(path)
            return

        for i in range(len(nums)):
            if visited[i] or (i >= 1 and nums[i] == nums[i - 1] and visited[i - 1] == False):
                continue

            if len(path) > 0 and self.isSquareful(path[-1] + nums[i]) == False:
                continue

            visited[i] = True
            self.dfs(nums, visited, path + [nums[i]], res)
            visited[i] = False

    def isSquareful(self, num):
        if num == 0 and num == 1:
            return True
        i = int(math.sqrt(num))
        return i * i == num




class Solution2:
    def numSquarefulPerms(self, A):
        n = len(A)
        count = collections.Counter(A)
        graph = {x: [] for x in count}
        # print(graph)
        for x in count:
            for y in count:
                if int(math.sqrt(x + y)) ** 2 == x + y:
                    graph[x].append(y)

        # print(graph)
        # i is position where we up to
        def dfs(node, i):
            count[node] -= 1
            if i == n - 1:
                res = 1
            else:
                res = 0
                for nei in graph[node]:
                    if count[nei]:
                        res += dfs(nei, i + 1)
            count[node] += 1
            return res

