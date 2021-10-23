"""
https://leetcode.com/problems/count-number-of-special-subsequences/discuss/1375379/C%2B%2B-solution-oror-Top-down-DP
"""

import functools

class SolutionTLE:
    def countSpecialSubsequences(self, nums):
        mod = 10 ** 9 + 7
        @functools.lru_cache(None)
        def dfs(i, prev):
            if i >= len(nums):
                return prev == 2

            res = 0
            res += dfs(i + 1, prev)

            if nums[i] == prev:
                res += dfs(i + 1, prev)

            if prev == -1 and nums[i] == 0:
                res += dfs(i + 1, 0)
            if prev == 0 and nums[i] == 1:
                res += dfs(i + 1, 1)
            if prev == 1 and nums[i] == 2:
                res += dfs(i + 1, 2)

            res %= mod
            return res

        return dfs(0, -1)


class SolutionTony:
    def countSpecialSubsequences(self, nums) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(i, prev):
            if i >= len(nums):
                return prev == 2

            res = 0
            res += dfs(i + 1, prev)
            if (nums[i] == prev + 1) or (nums[i] == prev):
                res += dfs(i + 1, nums[i])

            return res % mod

        res = dfs(0, -1)
        dfs.cache_clear()
        return res



nums = [0,1,2,2]
a = SolutionTony()
print(a.countSpecialSubsequences(nums))
