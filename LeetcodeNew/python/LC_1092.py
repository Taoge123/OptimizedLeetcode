
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        m, n = len(str1), len(str2)
        dp = [[0 for i in range( n +1)] for j in range( m +1)]

        for i in range(1, m+ 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j = m, n
        res = []
        while i > 0 or j > 0:
            if i == 0:
                res.append(str2[j - 1])
                j -= 1
            elif j == 0:
                res.append(str1[i - 1])
                i -= 1
            elif str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i][j - 1] == dp[i][j]:
                res.append(str2[j - 1])
                j -= 1
            elif dp[i - 1][j] == dp[i][j]:
                res.append(str1[i - 1])
                i -= 1

        return "".join(res[::-1])




