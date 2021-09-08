# """
# s sssss
#
# """
#
# #
# # class Solution:
# #
# #     def pal(self, s):
# #         memo = {}
# #         return self.dfs(s, 0, len(s)-1, memo)
# #
# #     def dfs(self, s, i, j, memo):
# #         if i == j:
# #             memo[(i, j)] = True
# #             return True
# #
# #         for k in range(i+1, j):
# #             if s[i] == s[j] and self.dfs(s, i+1, j-1, memo):
# #                 memo[(i, j)] = True
# #                 return True
# #
# #         memo[(i, j)] = False
# #         return False
#
#
# class Solution:
#     def pal(self, s):
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#
#         for i in range(n):
#             for j in range(n):
#                 if i == j:
#                     dp[i][j] = True
#
#         for k in range(1, len(s)):
#             for i in range(len(s)-k):
#                 j = i + k - 1
#                 if s[i] == s[j] and dp[i+1][j-1]:
#                     dp[i][j] = True
#
#         return dp[0][-1]
#
# s = "aabbaa"
# a = Solution()
# print(a.pal(s))
#
#
#
# def test(s):
#     n = len(s)
#     dp = [[False for _ in range(n)] for _ in range(n)]
#
#     for j in range(n):
#         for i in range(j+1):
#             if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
#                 dp[i][j] = True
#     return dp
#
# s = "efe"
# print(test(s))

class Solution:
    def backPackII(self, m, A, V):
        memo = {}
        return self.dfs(A, V, 0, m, memo)

    def dfs(self, A, V, pos, weight, memo):
        if (pos, weight) in memo:
            return memo[(pos, weight)]
        if pos >= len(A):
            return 0
        if weight == 0:
            return 0

        if weight < 0:
            return -V[pos-1]

        take = self.dfs(A, V, pos+1, weight-A[pos], memo) + V[pos]
        no_take = self.dfs(A, V, pos+1, weight, memo)

        memo[(pos, weight)] = max(take, no_take)
        return memo[(pos, weight)]



m = 1
A = [2,3,5,7]
V = [1,5,2,4]
a = Solution()
print(a.backPackII(m, A, V))


