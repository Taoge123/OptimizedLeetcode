
"""
0-1 Knapsack problem 


There are G people in a gang, and a list of various crimes they could commit.

The i-th crime generates a profit[i] and requires group[i] gang members to participate.

If a gang member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least P profit,
and the total number of gang members participating in that subset of crimes is at most G.

How many schemes can be chosen?  Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:

Input: G = 5, P = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation:
To make a profit of at least 3, the gang could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
Example 2:

Input: G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation:
To make a profit of at least 5, the gang could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).

Note:

1 <= G <= 100
0 <= P <= 100
1 <= group[i] <= 100
0 <= profit[i] <= 100
1 <= group.length = profit.length <= 100

"""

"""
dp[person+x][profit+y] += d[person][profit]

"""


class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:

        dp = [[[0] * (P + 1) for i in range(G + 1)] for j in range(len(group) + 1)]
        mod = 10 ** 9 + 7
        # no person and no profit的方案有1种
        dp[0][0][0] = 1
        for k in range(1, len(group) + 1):
            g = group[k - 1]
            p = profit[k - 1]
            # for person
            for i in range(G + 1):
                # for profit, profit can be 0
                for j in range(P + 1):
                    dp[k][i][j] = dp[k - 1][i][j]
                    if i >= g:
                        pp = max(0, j - p)
                        dp[k][i][j] += dp[k - 1][i - g][pp]
                        dp[k][i][j] %= mod

        res = 0
        for i in range(G + 1):
            res += dp[-1][i][P]
            res %= mod
        return res























