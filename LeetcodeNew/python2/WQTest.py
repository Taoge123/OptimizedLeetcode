#
# import collections
# #
# class Solution:
#     def findShortestSubArray(self, nums):
#
#         count = {}
#         first = {}
#         last = {}
#         degree = 0
#         for i, num in enumerate(nums):
#             if num in count:
#                 count[num] += 1
#                 last[num] = i
#             else:
#                 count[num] = 1
#                 first[num] = i
#                 last[num] = i
#             degree = max(degree, count[num])
#         min_len = float('inf')
#         for num in count:
#             if count[num] == degree:
#                 min_len = min(min_len, last[num] - first[num] + 1)
#         return min_len
#
#
# def degreeOfArray(arr):
#     # Write your code here
#     table = {}
#     first, last = {}, {}
#     indegree = 0
#     res = float('inf')
#
#     for idx, num in enumerate(arr):
#         if num in table:
#             table[num] += 1
#             last[num] = idx
#         else:
#             table[num] = 1
#             first[num], last[num] = idx, idx
#
#         indegree = max(indegree, table[num] + 1)
#
#     for num in table.keys():
#         if table[num] == indegree:
#             res = min(res, table[num] - first[num] + 1)
#
#     return res
#
#
# nums = [1,1,2,1,2,2]
# a = Solution()
# print(a.findShortestSubArray(nums))
#
# # print(degreeOfArray(nums))
#

import collections
import itertools


class UFS(object):
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]

    def find(self, x):
        path = []
        while x != self.parents[x]:
            path.append(x)
            x = self.parents[x]
        for p in path:
            self.parents[p] = x
        return x

    def union(self, x, y):
        p, q = self.find(x), self.find(y)
        if p != q:
            self.parents[p] = q
        self.find(x)

import collections
import itertools


def f(n, affected, poisonous):
    ufs = UFS(n)
    for a, p in zip(affected, poisonous):
        ufs.union(a, p)

    candidates = collections.defaultdict(set)
    for k, v in enumerate(ufs.parents[1:], 1):
        candidates[v].add(k)
    for k in candidates:
        candidates[k].add(None)
    element = [sorted(filter(None, i)) for i in itertools.product(*candidates.values())]
    element = [i for i in element if i and i[-1] - i[0] + 1 == len(i)]
    return element
# print(f(4, [1,2],[3,4]))
print(len(f(8, [2,3,4,3], [8,5,6,4])))



