
"""
https://leetcode.com/problems/count-all-possible-routes/discuss/866175/Python-or-DFS-with-Memorization-WITH-some-explanation-or-BFS-with-TLE
"""

import functools


class Solution:
    def countRoutes(self, nums, start: int, finish: int, fuel: int) -> int:

        n = len(nums)
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(node, k):
            if k < 0:
                return 0

            res = 0
            if node == finish:
                res += 1

            for nei in range(n):
                if nei == node:
                    continue
                res += dfs(nei, k - abs(nums[nei] - nums[node]))

            return res % mod

        return dfs(start, fuel)



class SolutionBU:
    def countRoutes(self, locations, start: int, finish: int, fuel: int) -> int:
        dp = [[[0 for i in range(3)] for j in range(201)] for _ in range(201)]
        mod = 10 ** 9 + 7
        startPos = locations[start]
        finishPos = locations[finish]
        locations.sort()
        n = len(locations)

        startIdx, finishIdx = 0, 0
        for i in range(n):
            if locations[i] == startPos:
                startIdx = i
            if locations[i] == finishPos:
                finishIdx = i

        dp[fuel][startIdx][0] = 1

        for f in range(fuel, -1, -1):
            for c in range(n):
                if c > 0 and f + locations[c] - locations[c - 1] <= fuel:
                    gas = locations[c] - locations[c - 1]
                    dp[f][c][0] += dp[f + gas][c - 1][1] + dp[f + gas][c - 1][0]
                    dp[f][c][1] += dp[f + gas][c - 1][1] + dp[f + gas][c - 1][0]
                if c < n - 1 and f + locations[c + 1] - locations[c] <= fuel:
                    gas = locations[c + 1] - locations[c]
                    dp[f][c][0] += dp[f + gas][c + 1][2] + dp[f + gas][c + 1][0]
                    dp[f][c][2] += dp[f + gas][c + 1][2] + dp[f + gas][c + 1][0]

        dp[f][c][0] %= mod
        dp[f][c][1] %= mod
        dp[f][c][2] %= mod

        res = 0
        for f in range(fuel + 1):
            res = (res + dp[f][finishIdx][0]) % mod
        return res




class SolutionTLE:
    def countRoutes(self, locations, start: int, finish: int, fuel: int) -> int:
        dp = [[0 for i in range(101)] for j in range(201)]
        mod = 10 ** 9 + 7
        n = len(locations)
        dp[fuel][start] = 1

        for f in range(fuel, -1, -1):
            for c in range(n):
                for d in range(n):
                    if d == c:
                        continue
                    gas = abs(locations[d] - locations[c])
                    if f + gas <= fuel:
                        dp[f][c] = (dp[f][c] + dp[f + gas][d]) % mod

        res = 0
        for f in range(fuel + 1):
            res = (res + dp[f][finish]) % mod
        return res





