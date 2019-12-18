
#
# class Solution:
#     def __init__(self):
#         self.MODULO = 1000000007
#
#
#     def solution(self, H):
#         length = len(H)
#         nests = [[0, 0] for i in range(length)]
#
#         for i in range(length):
#             nests[i] = [i, H[i]]
#
#         nests = sorted(nests, key=lambda x: x[1])
#         ways = [[0 for i in range(length + 1)] for j in range(length + 1)]
#
#         for i in range(length-1, -1, -1):
#             ways[i][length] = 1
#
#         for i in range(length - 1, -1, -1):
#             for j in range(length-1, i, -1):
#                 res = 0
#                 for k in range(j+1, length+1):
#                     if (k == length or (nests[k][0]-nests[i][0]) * (nests[j][0] - nests[i][0]) < 0):
#                         res += ways[i][k]
#                         res %= self.MODULO
#                 ways[i][j] = res
#
#         res = 0
#         for i in range(length):
#             res += self.ways(i, ways, length)
#             res %= self.MODULO
#         return res
#
#     def ways(self, first, ways, length):
#         res = 0
#         for second in range(first+1, length+1):
#             res += ways[first][second]
#             res %= self.MODULO
#
#         return res
#
# H = [ 4, 6, 2, 1, 5 ]
# # H = [ 13, 2, 5 ]
# a = Solution()
# print(a.solution(H))




# class Solution:
#     def __init__(self):
#         self.MODULO = 1000000007


def solution(H):
    MOD = 1000000007
    n = len(H)
    dp = [[0, 0] for i in range(n)]

    for i in range(n):
        dp[i] = [i, H[i]]
    temp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    dp = sorted(dp, key=lambda x: x[1])
    for i in range(n-1, -1, -1):
        temp[i][n] = 1

    for i in range(n - 1, -1, -1):
        for j in range(n-1, i, -1):
            res = 0
            for k in range(j+1, n+1):
                if (k == n or (dp[k][0]-dp[i][0]) * (dp[j][0] - dp[i][0]) < 0):
                    res += temp[i][k]
                    res %= MOD
            temp[i][j] = res

    res = 0
    for i in range(n):
        res += calc(i, temp, n, MOD)
        res %= MOD
    return res


def calc(i, ways, n, MOD):
    res = 0
    for j in range(i+1, n+1):
        res += ways[i][j]
        res %= MOD

    return res

H = [ 4, 6, 2, 1, 5 ]
# H = [ 13, 2, 5 ]

print(solution(H))







