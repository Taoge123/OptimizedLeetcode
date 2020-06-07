"""
https://www.youtube.com/watch?v=V5eeRgQsr6o
"""
import math

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






