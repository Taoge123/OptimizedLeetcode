"""
https://leetcode.com/problems/toss-strange-coins/discuss/410230/Python-Bottom-Up-DP-with-Explanation


Explanation
dp[c][k] is the prob of tossing c first coins and get k faced up.
dp[c][k] = dp[c - 1][k] * (1 - p) + dp[c - 1][k - 1] * p)
where p is the prob for c-th coin.

https://leetcode.com/problems/toss-strange-coins/discuss/418317/Python3-Top-Down-DP-Easy-with-picture

Base case: If no coins have been tossed then the probability that zero coins are facing heads is 100%.

The probability that after tossing the first i coins j coins are facing heads is the sum of the following probabilities:

j - 1 coins are facing heads after i - 1 tosses and coins i faces heads
j coins are facing heads after i - 1 tosses and coin i does not face heads
dp[0][0] = 1
dp[i][j] = dp[i - 1][j - 1] * p[i] + dp[i - 1][j] * (1 - p[i])
i: coins tossed
j: coins facing heads
Example:

prob: [0.5, 0.3, 0.8, 0.15, 0.75], target: 4

dp  0           1           2           j

0   1           0           0
1   0.5         0.5         0
2   0.35        0.5         0.15
3   0.07        0.38        0.43
4   0.0595      0.3335      0.4225
5   0.014875    0.128       0.35575

i
The probability that 2 coins are facing heads after tossing coin 5 is:
dp[4][1] * p[4] + dp[4][2] * (1 - p[4]) = 0.3335 * 0.75 + 0.4225 * 0.25 = 0.250125 + 0.105625 = 0.35575

"""


class Solution:
    def probabilityOfHeads(self, prob, target: int) -> float:
        n = len(prob)
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # base cases
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] * (1 - prob[i - 1])

        # recurrence
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                #上一轮没投出head - dp[i - 1][j - 1], 这轮需要投出prob[i - 1]
                #上一轮投出了head - dp[i - 1][j - 1], 这轮不需要投出 （1 - prob[i - 1]）
                dp[i][j] = dp[i - 1][j - 1] * prob[i - 1] + dp[i - 1][j] * (1 - prob[i - 1])

        return dp[n][target]



