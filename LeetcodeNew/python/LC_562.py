"""
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
"""


import collections

class Solution:
    def longestLine(self, M) -> int:
        if not M or not M[0]:
            return 0

        res = 0
        dp = collections.defaultdict(int)

        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j]:
                    dp[i, j, 0] = dp[i,     j - 1, 0] + 1
                    dp[i, j, 1] = dp[i - 1, j    , 1] + 1
                    dp[i, j, 2] = dp[i - 1, j - 1, 2] + 1
                    dp[i, j, 3] = dp[i - 1, j + 1, 3] + 1

                    res = max(res, dp[i, j, 0], dp[i, j, 1], dp[i, j, 2], dp[i, j, 3])
        for k, v in dp.items():
            if k[-1] == 3:
                print(k, v)

        return res


M =[[0,1,1,0],
    [0,1,1,0],
    [0,0,0,1]]


a = Solution()
print(a.longestLine(M))



"""
(0, 0, 0) 0
(0, 1, 0) 1
(0, 2, 0) 2
(1, 0, 0) 0
(1, 1, 0) 1
(1, 2, 0) 2
(2, 2, 0) 0
(2, 3, 0) 1

(-1, 1, 1) 0
(0, 1, 1) 1
(-1, 2, 1) 0
(0, 2, 1) 1
(1, 1, 1) 2
(1, 2, 1) 2
(1, 3, 1) 0
(2, 3, 1) 1

(-1, 0, 2) 0
(0, 1, 2) 1
(-1, 1, 2) 0
(0, 2, 2) 1
(0, 0, 2) 0
(1, 1, 2) 1
(1, 2, 2) 2
(2, 3, 2) 3


(-1, 2, 3) 0
(0, 1, 3) 1
(-1, 3, 3) 0
(0, 2, 3) 1
(1, 1, 3) 2
(0, 3, 3) 0
(1, 2, 3) 1
(1, 4, 3) 0
(2, 3, 3) 1


"""



