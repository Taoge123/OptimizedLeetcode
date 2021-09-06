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
def test(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for i in range(j+1):
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
    return dp

s = "efe"
print(test(s))

