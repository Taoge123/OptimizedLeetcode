
class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "":
            return 0
        n = len(s)
        dp = [0 for x in range( n +1)]
        dp[0] = 1

        for i in range(1, n + 1):
            if s[ i -1] != '0':
                dp[i] += dp[ i -1]
            if i != 1 and s[ i -2:i] >= "10" and s[ i -2:i] <= "26":
                dp[i] += dp[ i -2]

        return dp[-1]





