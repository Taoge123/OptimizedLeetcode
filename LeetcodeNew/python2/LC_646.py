"""
[[1,2], [2,3], [3,4]]


"""


class Solution:
    def findLongestChain(self, pairs) -> int:

        pairs.sort()
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)




