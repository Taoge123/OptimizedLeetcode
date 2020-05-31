#
# class Solution:
#     def maxEvents(self, events) -> int:
#         events = sorted(events)
#         res = 1
#         visited = set()
#         visited.add(events[0][0])
#         for i in range(1, len(events)):
#             if events[i - 1][1] >= events[i][0] and (events[i - 1][1] not in visited or events[i][0] not in visited):
#                 res += 1
#                 visited.add(events[i - 1][1])
#
#         return res
#
#
#
#
# events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
# a = Solution()
# print(a.maxEvents(events))
# #
# import collections
#
# class Solution:
#     def isPossible(self, target) -> bool:
#         nums = [1] * len(target)
#         queue = collections.deque()
#         queue.append(nums)
#         visited = set()
#         visited.add(tuple(nums))
#
#         while queue:
#             node = queue.popleft()
#             print(node)
#             if max(node) > max(target):
#                 continue
#             if collections.Counter(node) == collections.Counter(target):
#                 return True
#             summ = sum(node)
#             if summ > max(target):
#                 continue
#             for i in range(len(nums)):
#                 temp = node[i]
#                 node[i] = summ
#                 print(sorted(tuple(node)))
#                 if set(sorted(tuple(node))) not in visited:
#                     visited.add(tuple(sorted(node[:])))
#                     queue.append(node[:])
#                 node[i] = temp
#         return False
#
# target = [1,1384,1,1,10,2767,379,1,217,1]
# # target = [8,5]
# a = Solution()
# print(a.isPossible(target))
#

# class Solution:
#     def generateTheString(self, n: int) -> str:
#         if n % 2 == 1:
#             return n * 'a'
#         else:
#             return 'a' +(n-1) * b
#
#
# class Solution:
#     def numTimesAllBlue(self, light) -> int:
#         if not light:
#             return 1
#
#         res = 0
#         preSum = [1]
#         n = len(light)
#         for i in range(2, n + 1):
#             preSum.append(i + preSum[-1])
#
#         newLight = [light[0]]
#         for i in range(1, n):
#             newLight.append(light[i] + newLight[-1])
#
#         for i, j in zip(preSum, newLight):
#             if i == j:
#                 res += 1
#         return res
#
# light = [1,2,3,4,5,6]
# a = Solution()
# print(a.numTimesAllBlue(light))
#


# class Solution:
#     def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
#         cache = {}
#         return max(self.cost(cache, n, i, headID, manager, informTime) for i in range(n))
#
#     def cost(self, cache, n, index, headID, manager, informTime):
#         if cache.get(index):
#             return cache[index]
#         else:
#             if index == headID:
#                 return 0
#
#             curr = informTime[manager[index]]
#             next = self.cost(cache, n, manager[index], headID, manager, informTime)
#             cache[index] = curr + next
#             return cache[index]
#
#
# n = 6
# headID = 2
# manager = [2,2,-1,2,2,2]
# informTime = [0,0,1,0,0,0]
#
#
#
# # n = 7
# # headID = 6
# # manager = [1,2,3,4,5,6,-1]
# # informTime = [0,6,5,4,3,2,1]
#
# a = Solution()
# print(a.numOfMinutes(n, headID, manager, informTime))
#

#
# import collections
#
# class Solution:
#     def frogPosition(self, n: int, edges, t: int, target: int) -> float:
#         graph = collections.defaultdict(list)
#         summ = 1
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
#         visited = set()
#         self.dfs(graph, 1, None, t, target, summ, visited)
#         return 1/summ
#     def dfs(self, graph, i, parent, t, target, summ, visited):
#         print(i, t)
#
#         if t < 0:
#             return 0
#
#         if i == target and t >= 0:
#             return 1 / summ
#
#         summ = summ * len(graph[i])
#         visited.add(i)
#         for j in graph[i]:
#             if j not in visited:
#                 self.dfs(graph, j, parent, t, target, summ, visited)
#
#
# n = 7
# edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
# t = 1
# target = 7
#
# a = Solution()
# print(a.frogPosition(n, edges, t, target))
#
#
#
# """
#
# 91  93 89 88 100 112
#  0  1  2  3  4   5
#
# """
#
# def hashKey(timestamp):
#     timestamp = timestamp.split(':')
#     return int(timestamp[-1]) + int(timestamp[-2]) * 60 + int(timestamp[-3]) * 60 * 60
#

import bisect

#
# class Solution:
#     def longestSubarray(self, nums, limit: int) -> int:
#         temp = []
#         for i in range(len(nums) - 1):
#             temp.append(nums[i + 1] - nums[i])
#
#         print(temp)
#         left = 0
#         count = 0
#         summ = 0
#         res = 0
#         for i, num in enumerate(temp):
#             if abs(num) > limit:
#                 count = 0
#                 summ = 0
#                 left = i + 1
#             else:
#                 while abs(summ) > limit:
#                     summ -= nums[left]
#                     count -= 1
#                     left += 1
#                 else:
#                     count += 1
#                     summ += num
#                     if abs(summ) <= limit:
#                         res = max(res, count)
#         return res + 1
#
#
# # nums = [4,2,2,2,4,4,2,2]
# # limit = 0
# # nums = [8,2,4,7]
# # limit = 4
# # nums = [8,2,4,7]
# # # [-6, 2, 3]
# # #      2  3
# # limit = 4
#
# nums = [4,8,5,1,7,9]
# limit = 6
# a = Solution()
# print(a.longestSubarray(nums, limit))
#


# class Solution:
#     def buildArray(self, target, n: int):
#
#         if len(target) > n:
#             return []
#
#         res = []
#         i = 0
#         num = 1
#         while i < len(target):
#             print(i)
#             if target[i] == num:
#                 res.append('push')
#                 i += 1
#                 num += 1
#             else:
#                 while i < len(target) and target[i] != num:
#                     res.append('push')
#                     res.append('pop')
#                     num += 1
#                 res.append('push')
#                 i += 1
#                 num += 1
#         return res
#
#
#
# target = [2, 3, 4]
# n = 4
# a = Solution()
# print(a.buildArray(target, n))

import collections

#
# class Solution:
#     def minTime(self, n: int, edges, hasApple) -> int:
#         graph = collections.defaultdict(list)
#         for u, v in edges:
#             graph[u].append(v)
#             # graph[v].append(u)
#
#         targets = []
#         for i, val in enumerate(hasApple):
#             if val:
#                 targets.append(i)
#
#         self.sum = 0
#         for target in targets:
#             self.dfs(graph, 0, target, 0)
#         return self.sum
#
#     def dfs(self, graph, root, target, step):
#         if root == target:
#             self.sum += step * 2
#             return
#
#         for nei in graph[root]:
#             self.dfs(graph, nei, target, step + 1)


class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            # graph[v].append(u)

        targets = []
        for i, val in enumerate(hasApple):
            if val:
                targets.append(i)

        self.sum = 0
        for target in targets:
            self.dfs(graph, 0, target, 0)
        return self.sum

    def dfs(self, graph, root, target, step):
        if root == target:
            self.sum += step * 2
            return

        for nei in graph[root]:
            self.dfs(graph, nei, target, step + 1)


class Solution2:
    def minTime(self, n: int, edges, hasApple) -> int:
        # graph = collections.defaultdict(list)

        graph = [[float('inf') for i in range(n)] for j in range(n)]
        for u, v in edges:
            # graph[u].append([v, 1])
            # graph[v].append(u)
            graph[u][v] = 1
            graph[v][u] = 1

        targets = []

        for i, val in enumerate(hasApple):
            if val:
                targets.append(i)

        dist = self.dfs(graph)
        print(dist)
        print(targets)


    def dfs(self, graph):
        dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
        n = len(graph)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist

"""
[2, 1, 1, 2, 2, 2, 2], 
[1, 2, 2, 3, 1, 1, 3], 
[1, 2, 2, 1, 3, 3, 1], 
[2, 3, 1, 2, 4, 4, 2], 
[2, 1, 3, 4, 2, 2, 4], 
[2, 1, 3, 4, 2, 2, 4], 
[2, 3, 1, 2, 4, 4, 2]

0 2 4 5
"""

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]


a = Solution2()
print(a.minTime(n, edges, hasApple))


