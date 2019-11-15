


# def findlargestSubGrid(grid, maxSum):
#     global len
#     if not grid or not maxSum:
#         return 0
#     m = len(grid)
#     n = len(grid[0])
#     if (m != n):
#         return 0
#     dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
#     ret = [0 for i in range(m)]
#     for i in range(m):
#         for j in range(n):
#             dp[i + 1][j + 1] = grid[i][j] +  dp[i + 1][j] + dp[i][j + 1] - dp[i][j]
#
#     length = len(dp)
#     for len in range(m+1):
#         max = float('-inf')
#         for i in range(len, length):
#             for j in range(len, length):
#                 max = max(max, dp[i][j] - dp[i - len][j] - dp[i][j - len] + dp[i - len][j - len])
#         ret[len-1] = max
#
#     for i in range(len(ret)-1, -1, -1):
#         if (ret[i] <= maxSum):
#             return i + 1
#
# grid = [[2,2,2], [3,3,3], [4,4,4]]
# maxSum = 28
#
# print(findlargestSubGrid(grid, maxSum))
#

# def solution(A, B):
#     # write your code in Python 3.6
#
#     sumn = A * B
#     binNum = bin(sumn)[2:]
#     print(binNum)
#     return binNum
#
# solution(3, 7)

import collections
import math

def solution(A):
    # write your code in Python 3.6
    table = collections.defaultdict(int)
    res = []
    final = 0
    for i, val in enumerate(A):
        table[val] += 1
    print(table)

    for k, v in table.items():
        if v >= 2:
            res.append(v)

    for val in res:
        final += helper(val)

    return final

def helper(val):
    if val < 2:
        return 0
    if val == 2:
        return 1
    else:
        m = math.factorial(val) // (math.factorial(val-2) * math.factorial(2))


# solution([3,5,6,3,3,5])
val = 4
print(math.factorial(val) // (math.factorial(val-2) * math.factorial(2)))




