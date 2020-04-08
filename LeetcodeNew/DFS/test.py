#
#
#
# # def findlargestSubGrid(grid, maxSum):
# #     global len
# #     if not grid or not maxSum:
# #         return 0
# #     m = len(grid)
# #     n = len(grid[0])
# #     if (m != n):
# #         return 0
# #     dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
# #     ret = [0 for i in range(m)]
# #     for i in range(m):
# #         for j in range(n):
# #             dp[i + 1][j + 1] = grid[i][j] +  dp[i + 1][j] + dp[i][j + 1] - dp[i][j]
# #
# #     length = len(dp)
# #     for len in range(m+1):
# #         max = float('-inf')
# #         for i in range(len, length):
# #             for j in range(len, length):
# #                 max = max(max, dp[i][j] - dp[i - len][j] - dp[i][j - len] + dp[i - len][j - len])
# #         ret[len-1] = max
# #
# #     for i in range(len(ret)-1, -1, -1):
# #         if (ret[i] <= maxSum):
# #             return i + 1
# #
# # grid = [[2,2,2], [3,3,3], [4,4,4]]
# # maxSum = 28
# #
# # print(findlargestSubGrid(grid, maxSum))
# #
#
# # def solution(A, B):
# #     # write your code in Python 3.6
# #
# #     sumn = A * B
# #     binNum = bin(sumn)[2:]
# #     print(binNum)
# #     return binNum
# #
# # solution(3, 7)
#
# import collections
# import math
#
# def solution(A):
#     # write your code in Python 3.6
#     table = collections.defaultdict(int)
#     res = []
#     final = 0
#     for i, val in enumerate(A):
#         table[val] += 1
#     print(table)
#
#     for k, v in table.items():
#         if v >= 2:
#             res.append(v)
#
#     for val in res:
#         final += helper(val)
#
#     return final
#
# def helper(val):
#     if val < 2:
#         return 0
#     if val == 2:
#         return 1
#     else:
#         m = math.factorial(val) // (math.factorial(val-2) * math.factorial(2))
#
#
# # solution([3,5,6,3,3,5])
# val = 4
# print(math.factorial(val) // (math.factorial(val-2) * math.factorial(2)))


# class Solution:
#     def numSteps(self, s: str) -> int:
#         n = len(s)
#         b = bin(int(s))[-4:]
#         temp = 0
#         for i, num in enumerate(s[::-1]):
#             if num == '1':
#                 temp += 2 ** i
#
#
#         # b = int(b)
#         count = 0
#         while temp != 1:
#             if temp & 1 == 1:
#                 temp += 1
#             else:
#                 temp >>= 1
#             count += 1
#
#         return count
#
#
# s = "10"
# a = Solution()
# print(a.numSteps(s))
#


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = ['a', 'b', 'c']
        queue = [['a', a], ['b', b], ['c', c]]
        res = ""
        while queue:
            print(queue)
            node = queue.pop(0)
            if node == 1:
                if node == 'a' and res[-1] != 'a':
                    res += 'a'
                elif node == 'b' and res[-1] != 'b':
                    res += 'b'
                elif node == 'c' and res[-1] != 'c':
                    res += 'c'
            if node == 2:
                if node == 'a' and res[-1] != 'a':
                    res += node * 'a'
                elif node == 'b' and res[-1] != 'b':
                    res += node * 'b'
                elif node == 'c' and res[-1] != 'c':
                    res += node * 'c'
            else:
                if node == 'a' and res[-1] != 'a':
                    res += 2 * 'a'
                elif node == 'b' and res[-1] != 'b':
                    res += 2 * 'b'
                elif node == 'c' and res[-1] != 'c':
                    res += 2 * 'c'
                node -= 2
                if node > 0:
                    queue.append(node)
        return res



a = Solution()
print(a.longestDiverseString(7, 1, 1))