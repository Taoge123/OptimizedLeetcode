
"""
https://leetcode-cn.com/problems/largest-divisible-subset/solution/jian-yi-ban-ji-yi-hua-dfs-by-luo-bi-da-q-cyxd/

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""

"""
1 2 3 4 9 36
          i
    j
if nums[i] % nums[j] == 0:
    dp[i] = dp[j] + 1
    parent[i] = j

"""

import functools


class SolutionTony2:
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        nums = sorted(nums) + [1]

        @functools.lru_cache(None)
        def dfs(i):
            res = []
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[j]] + dfs(j)
                    if len(tmp) > len(res):
                        res = tmp
            return res

        return dfs(-1)


class SolutionTony1:
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        nums = sorted(nums)

        @functools.lru_cache(None)
        def dfs(i, num):
            res = []
            for j in range(i, n):
                if nums[j] % num == 0:
                    tmp = [nums[j]] + dfs(j + 1, nums[j])
                    if len(tmp) > len(res):
                        res = tmp
            return res

        return dfs(0, 1)


class SolutionWisdom:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        n = len(nums)
        nums.sort()
        dp = [1 for i in range(n)]
        parent = [-1 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] == dp[j] + 1:
                        parent[i] = j

        length = 0
        idx = 0
        for i in range(n):
            if dp[i] > length:
                length = dp[i]
                idx = i

        res = []
        while idx != -1:
            res.append(nums[idx])
            idx = parent[idx]

        return res




class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums = sorted(nums)
        n = len(nums)
        parent = [-1] * n
        dp = [0] * n
        maxi, index = 0, 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] >= maxi:
                        maxi = dp[i]
                        index = i

        res = []
        while index != -1:
            res.append(nums[index])
            index = parent[index]
        return res






