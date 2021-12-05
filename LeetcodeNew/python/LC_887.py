"""
1. broken : we have K-1 egges left, and we know 0<=F<i, i-1 (1~i-1) floors left -> D(K-1, i-1)
1. Unbroken : we still have K eggs, and we know 0<=F<=N, N-i (i+1~N) floors left -> D(K, N-i)

We need to know the worst case -> max(D(K-1, i), D(K, N-i))

"""

from functools import lru_cache

"""

|
|
|
|

k == 1 : return n

|
n == 1: return 1


|
|
| 3
 |
|
| 2
|




|
|
|
|

k == 2: 

dfs(2, 4)
1 -> dfs(1, 0), dfs(2, 3)
2 -> dfs(1, 1), dfs(2, 2)
3 -> dfs(1, 2), dfs(2, 1)
4 ->

"""

import functools


class SolutionBS1:
    def superEggDrop(self, k: int, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(k, n):
            if k == 1:
                return n
            if n <= 1:
                return n

            left, right = 1, n
            res = float('inf')
            while left < right:
                mid = (left + right) // 2
                down = dfs(k - 1, mid - 1)
                up = dfs(k, n - mid)
                maxi = max(down, up) + 1
                if down < up:
                    left = mid + 1
                else:
                    right = mid
                res = min(res, maxi)
            return res

        return dfs(k, n)



class SolutionTLE:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = [[float('inf') for i in range(N + 1)] for j in range(K + 1)]

        @lru_cache(None)
        def dfs(k, n):
            if k == 0:
                return 0
            if k == 1:
                return n
            if n <= 1:
                return n
            res = memo[k][n]
            for i in range(1, n + 1):
                res = min(res, 1 + max(dfs(k - 1, i - 1), dfs(k, n - i)))
            return res

        return dfs(K, N)



class SolutionLee:
    def superEggDrop(self, K, N):
        dp = [[0] * (K + 1) for i in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][K] >= N:
                return m



class SolutionBS:
    def superEggDrop(self, k: int, n: int) -> int:

        memo = {}
        return self.dfs(k, n, memo)

    def dfs(self, k, n, memo):
        if (k, n) in memo:
            return memo[(k, n)]

        if k == 1:
            return n
        if n <= 1:
            return n

        left, right = 1, n
        res = float('inf')
        while left < right:
            mid = (left + right) // 2
            down = self.dfs(k - 1, mid - 1, memo)
            up = self.dfs(k, n - mid, memo)
            maxi = max(down, up) + 1
            if down < up:
                left = mid + 1
            else:
                right = mid
            res = min(res, maxi)
        memo[(k, n)] = res
        return res
