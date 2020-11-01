"""
dp[i][k] : the minimum cost of deletions for the first i elements, and the remaining ending element is k

dp[i][k]
1. dp[i-1][k] + cost[i]
2. if (s[i] == k): min(dp[i-1][k'] + (cost is 0))


----------------------------------------------------------------------------------------------------------------

OOXOOXOOXOOXOOXOOX

"""



class Solution:
    def minCost(self, s: str, cost) -> int:
        stack = []
        i = 0
        res = 0
        while i < len(s):
            j = i
            summ = 0
            maxi = 0
            while j < len(s) and s[i] == s[j]:
                summ += cost[j]
                maxi = max(maxi, cost[j])
                j += 1

            res += summ - maxi
            i = j
        return res




class SolutionGreddy2:
    def minCost(self, s: str, cost) -> int:
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(i)
            else:
                if s[stack[-1]] != s[i]:
                    stack.append(i)
                else:
                    if cost[stack[-1]] < cost[i]:
                        stack.pop()
                        stack.append(i)
                    else:
                        continue
        return sum(cost) - sum([cost[i] for i in stack])












