# # # def test(bids):
# # #     temp = sorted(bids, key=lambda x: (x[-2], -x[-1]), reverse=True)
# # #     table = collections.defaultdict(list)
# # #     for i, item in enumerate(temp):
# # #         if item[2] not in table:
# # #             table[item[2]].append([item[3], [1, item[1]]])
# # #         else:
# # #             node = table[item[2]]
# # #             id = [node[0][0]].append([item[3]])
# # #             del table[item[2]]
# # #             table[item[2]].append([id, [node[0][-1][0] + 1, node[0][-1][1] + item[1]]])
# # #
# # #     for i, j in table.items():
# # #         print(i, j)
# # #     heapq.heapify(bids)
# # #     print(bids)
# #
# #
# #
# # import heapq
# # import collections
# #
# # bids = [
# #         [3, 7, 5, 3],
# #         [3, 7, 5, 2],
# #         [3, 7, 5, 1],
# #         [1, 5, 5, 0],
# #         [2, 7, 8, 1],
# #         [4, 10,3, 3],
# #         ]
# #
# # # def test(bids, totalShare):
# # #     temp = sorted(bids, key=lambda x: (x[-2], -x[-1]), reverse=True)
# # #     res = []
# # #     table = collections.defaultdict(list)
# # #     for i, item in enumerate(temp):
# # #         if item[2] not in table:
# # #             table[item[2]]  = [[item[0], item[1]]]
# # #         else:
# # #             table[item[2]].append([item[0], item[1]])
# # #
# # #     for k, v in table.items():
# # #         heapq.heappush(res, (-k, v))
# # #
# # #     final = []
# # #     for i in range(len(res)):
# # #         final.append(heapq.heappop(res)[-1])
# # #
# # #     for i in final:
# # #         print(i)
# # #
# # #     for i, node in enumerate(final):
# # #         lower = len(node)
# # #         upper = sum(i[1] for i in node)
# # #
# # #         if totalShare < lower:
# # #             return [node[0] for node in final[i][totalShare:]] + [i[0] for node in final[i+1:] for i in node ]
# # #         elif lower <= totalShare <= upper:
# # #             return [i[0] for node in final[i+1:] for i in node ]
# # #         else:
# # #             totalShare -= upper
# #
# #
# # totalShares = 17
# # bids.sort(key=lambda x: x[2], reverse=True)
# # # 8,5,5,3
# # ret = []
# # i = 0
# #
# # while i < len(bids):
# #     # start the new price list
# #     curr_min_price = bids[i][2]
# #     curr_price_list = []
# #     while i < len(bids) and bids[i][2] == curr_min_price:
# #         curr_price_list.append(bids[i])
# #         i += 1
# #     ret.append(curr_price_list)
# #
# # for i in ret:
# #     i.sort(key=lambda x: x[3])
# #
# # remain = totalShares
# # final_idx = []
# #
# # for i in range(len(ret)):
# #     curr_lower = len(ret[i])
# #     curr_upper = sum([e[1] for e in ret[i]])
# #     if remain < curr_lower:  # e.g. 3, 4
# #         final_idx += [e[0] for e in ret[i][remain:]] + [e[0] for k in ret[i + 1:] for e in k]
# #         break
# #     elif curr_lower <= remain <= curr_upper:
# #         final_idx = [e[0] for k in ret[i + 1:] for e in k]
# #         break
# #     elif remain > curr_upper:
# #         remain -= curr_upper
# # print(final_idx)
# #
# #
# #
# # """
# # http:request
# #
# #
# #
# # """
# #
# #
# #
# #
#
#
# #
# # A = [1,2,3,4,5,6,7,8]
# #
# # for i in range(len(A)):
# #     left = A[:i:-1]
# #     right = A[:i]
# #     print(left, right)
#
#
# # def countPairs(arr, k):
# #     # Write your code here
# #     arr = sorted(arr)
# #
# #     left = 0
# #     right = len(arr) - 1
# #     res = 0
# #
# #     while left < right:
# #         summ = arr[left] + arr[right]
# #         if summ < k:
# #             left += 1
# #         elif summ > k:
# #             right -= 1
# #         else:
# #             res += 1
# #             while left <= right and arr[left + 1] == arr[left]:
# #                 res += 1
# #                 left += 1
# #                 break
# #             while left <= right and arr[right - 1] == arr[right]:
# #                 res += 1
# #                 right -= 1
# #                 break
# #         left += 1
# #         right -= 1
# #
# #     return res
#
#
# def countPairs(arr, k):
#     n = len(arr)
#     count = 0
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             if arr[i] + arr[j] == k:
#                 count += 1
#
#     return count
#
#
# # arr = [5,7,9,13,11,6,6,3,3]
# # k = 12
# # arr = [1,3,46,1,3,9]
# # k = 47
# #
# # print(countPairs(arr, k))
#
#
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
# #
# # class Solution:
# #     def flatten(self, root: TreeNode) -> None:
# #         dummy = TreeNode(0)
# #         self.prev = dummy
# #         self.pre_order(root)
# #
# #         ptr = dummy
# #         while ptr:
# #             ptr.left = None
# #             ptr.right = ptr.next
# #             del ptr.next
# #             ptr = ptr.right
# #         return dummy
# #
# #     def pre_order(self, root):
# #         if not root:
# #             self.prev.next = None
# #             return
# #
# #         self.prev.next = root
# #         self.prev = root
# #         self.pre_order(root.left)
# #         self.pre_order(root.right)
# #
# #
# # class Solution:
# #    def __init__(self):
# #        self.prev = None
# #
# #
# #    def flatten(self, root: TreeNode) -> None:
# #        if not root:
# #            return None
# #
# #        self.flatten(root.left)
# #        self.flatten(root.right)
# #        root.right = self.prev
# #        root.left = None
# #        self.prev = root
#
# class Solution:
#    def kthSmallest(self, root: TreeNode, k: int) -> int:
#        self.k = k
#        self.res = 0
#        self.helper(root)
#        return self.res
#
#    def helper(self, root):
#        if not root:
#            return
#        print(root.val)
#        self.helper(root.left)
#        self.k -= 1
#        if self.k == 0:
#            self.res = root.val
#        if self.k <= 0:
#            return
#        self.helper(root.right)
#
# """
#      5
#    3    7
#   2 4  6  8
#
# """
#
# root = TreeNode(5)
# root.left= TreeNode(3)
# root.right= TreeNode(7)
# root.left.left= TreeNode(2)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(8)
#
# a = Solution()
# print(a.kthSmallest(root, 3))
#
#
#
# import math
#
# def find(n):
#     res = 0
#     for i in range(1, int(math.sqrt(n)) + 1):
#         x = i
#         y = math.ceil(n / x)
#         print(x, y, x*y)
#         res = min(res, x + y)
#     return x, y
#
# n = 100
# print(find(n))
# class Solution:
#
#     def __init__(self):
#         self.count = 0
#     def can_partition(self, num):
#          s = sum(num)
#          dp = [[-1 for x in range(s+1)] for y in range(len(num))]
#
#          ans = self.can_partition_recursive(dp, num, 0, 0, 0)
#          # print(dp)
#          print(self.count)
#          return ans
#
#     def can_partition_recursive(self, dp, num, currentIndex, sum1, sum2):
#         # base check
#         # print(currentIndex, sum1, sum2)
#         self.count += 1
#         if currentIndex == len(num):
#             return abs(sum1 - sum2)
#
#         # check if we have not already processed similar problem
#         if dp[currentIndex][sum1] == -1:
#             # recursive call after including the number at the currentIndex in the first set
#             diff1 = self.can_partition_recursive(
#                 dp, num, currentIndex + 1, sum1 + num[currentIndex], sum2)
#
#             # recursive call after including the number at the currentIndex in the second set
#             diff2 = self.can_partition_recursive(
#                 dp, num, currentIndex + 1, sum1, sum2 + num[currentIndex])
#
#             dp[currentIndex][sum1] = min(diff1, diff2)
#         else:
#             # retrieve memo value
#             print(currentIndex, sum1, sum2)
#
#         return dp[currentIndex][sum1]
#
#
# num = [1, 10000, 1000000]
# a = Solution()
# print(a.can_partition(num))
#
"""

"""
"""
rating = [2,5,3,4,1]

  2, 5, 3, 4, 1
  1  2  2  3  1
             i                 

  1  4  3  5  2
  1  2  2  4  2
             i
             
   2 1 3
   1 1 2
   
"""

#
# class Solution:
#     def numTeams(self, rating) -> int:
#         a = self.find(rating)
#         temp = rating[::-1]
#         b = self.find(temp)
#         res = 0
#         for num in a + b:
#             if num >= 3:
#                 res += num - 2
#
#         return res
#
#     def find(self, nums):
#
#         if not nums:
#             return []
#         dp = [1 for i in range(len(nums))]
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#
#         return dp


#
# class Solution:
#     def numTeams(self, nums) -> int:
#         res = []
#         self.dfs1(nums, 0, [], res)
#         res2 = []
#         self.dfs2(nums[::-1], 0, [], res2)
#
#         final = set()
#         for num in res + res2:
#             final.add(tuple(sorted(num)))
#         for i in final:
#             print(i)
#         return len(final)
#
#
#     def dfs1(self, nums, index, path, res):
#         if len(path) == 3:
#             res.append(path[:])
#
#         for i in range(index, len(nums)):
#             if not path:
#                 path.append(nums[i])
#                 self.dfs1(nums, index + 1, path, res)
#                 path.pop()
#             else:
#                 if nums[i] > path[-1]:
#                     path.append(nums[i])
#                     self.dfs1(nums, i, path, res)
#                     path.pop()
#
#
#     def dfs2(self, nums, index, path, res):
#         if len(path) == 3:
#             res.append(path[:])
#
#         for i in range(index, len(nums)):
#             if not path:
#                 path.append(nums[i])
#             else:
#                 if nums[i] > path[-1]:
#                     path.append(nums[i])
#                     self.dfs2(nums, i, path, res)
#                     path.pop()
#
#
#
# nums = [4,7,9,5,10,8,2,1,6]
#
#
#
#
# # nums = [2,1,3]
# a = Solution()
# print(a.numTeams(nums))
#
#
#


"""
id : {place1: 15
      place2: 20
       }
       
place1: {
      id: 12
 }

id : 1, 2
(1, 2) - ()

"""

import collections

class UndergroundSystem:

    def __init__(self):
        self.ids = collections.defaultdict(list)
        self.average1 = collections.defaultdict(int)
        self.average2 = collections.defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id].append([stationName, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.ids[id][-1].append(stationName)
        startStation = self.ids[id][-1][0]
        time = self.ids[id][-1][1]
        self.average1[[startStation, stationName]] += t - time
        self.average2[[startStation, stationName]] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.average1[startStation, endStation] / self.average2[startStation, endStation]























