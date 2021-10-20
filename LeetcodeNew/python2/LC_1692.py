"""
https://leetcode.com/problems/count-ways-to-distribute-candies/discuss/975023/Java-dfs%2Bmemo
https://leetcode.com/problems/count-ways-to-distribute-candies/discuss/976136/Bottom-Up-Top-Down-Linear-space-JavaPython
https://leetcode.com/problems/count-ways-to-distribute-candies/discuss/974974/C%2B%2B-and-Python3-bottom-up-DP-O(n-*-k)-clean-code-with-explanation
https://leetcode.com/problems/count-ways-to-distribute-candies/discuss/1477126/Python-DP-with-detailed-explanation
https://leetcode.com/problems/count-ways-to-distribute-candies/discuss/981039/python3-with-explanation


1. For dp[n][k], first think of the previous state without the current candy (eg. the nth candy)
a. If there are already n-1 candies put in k bags, then the nth candy can be put in any one of the k bag
-> so a total of k * dp[n-1][k] possibilities
b. If there are n-1 candies put in k-1 bags, then the nth candy must be put in the kth bag
-> so a total of dp[n-1][k-1] possibilites
2. Sum up the possibilities in 2 cases and be ware of the modulo to get the result
3. Can use global array for memoization because the result will be the same for the same n and k

"""

import functools


class SolutionTony:
    def waysToDistribute(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(n, k):
            if n == 0 and k == 0:
                return 1

            if n == 0 or k == 0 or n < k:
                return 0

            # n - 1 are all distributed in k bages, last one can be put in any bag
            anybag = dfs(n - 1, k) * k

            # n - 1 are all distributed in k - 1 bages, last one can only be put in last bag
            lastbag = dfs(n - 1, k - 1)

            return (anybag + lastbag) % mod

        res = dfs(n, k) % mod
        dfs.cache_clear()
        return res


class SolutionTD:
    def waysToDistribute(self, n: int, k: int) -> int:

        mod = 10 ** 9 + 7
        self.n = n
        self.k = k

        @functools.lru_cache(None)
        def dfs(n, k):
            if k > n or k > self.k:
                return 0

            if n >= self.n:
                if k == self.k:
                    return 1
                return 0

            res = 0
            res += dfs(n + 1, k + 1)
            res += k * dfs(n + 1, k)
            return res % mod

        res = dfs(0, 0) % mod
        dfs.cache_clear()
        return res


class Solution2:
    def waysToDistribute(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(n, k):
            if n == 0:
                return 0
            if k == 1:
                return 1
            return dfs(n - 1, k - 1) + k * dfs(n - 1, k)

        res = dfs(n, k) % mod
        dfs.cache_clear()
        return res


