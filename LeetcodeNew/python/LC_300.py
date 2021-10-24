"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

"""

import bisect
import functools


class SolutionTD1:
    def lengthOfLIS(self, nums) -> int:

        n = len(nums)
        @functools.lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0
            res = 0
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    res = max(res, dfs(j) + 1)

            return res

        res = 0
        for i in range(n):
            res = max(res, dfs(i) + 1)

        return res



class SolutionMLE:
    def lengthOfLIS(self, nums) -> int:

        n = len(nums)

        @functools.lru_cache(None)
        def dfs(prev, i):
            if i >= n:
                return 0

            take, no_take = 0, 0
            if prev < 0 or nums[prev] < nums[i]:
                take = dfs(i, i + 1) + 1
            no_take = dfs(prev, i + 1)

            return max(take, no_take)

        return dfs(-1, 0)


class Solution:
    def longestIncreasingSubsequence(self, nums):
        res = 0
        memo = {}
        for i in range(len(nums)):
            res = max(res, 1+self.dfs(nums, i, memo))
        return res

    def dfs(self, nums, i, memo):
        n = len(nums)
        if i == n:
            return 0
        if i in memo:
            return memo[i]
        res = 0
        for j in range(i+1, n):
            if nums[j] > nums[i]:
                res = max(res, self.dfs(nums, j, memo) + 1)
        memo[i] = res
        return res



class SolutionTony:
    def longestIncreasingSubsequence(self, nums):
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i):
            if i == n:
                return 0
            res = 0
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    res = max(res, dfs(j) + 1)
            return res

        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i) + 1)
        return res


import functools


class SolutionRika:
    def longestIncreasingSubsequence(self, nums):
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i):
            if i == n:
                return 0
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j) + 1)
            return res

        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i) + 1)
        return res



class SolutionOp:
    def lengthOfLIS(self, nums):

        dp = []
        for num in nums:
            i = bisect.bisect_left(dp, num)
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
        return len(dp)



class SolutionTest:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0

        dp = []
        for i, num in enumerate(nums):
            index = self.bisect_left(dp, num)
            if index >= len(dp):
                dp.append(num)
            else:
                dp[index] = num
        return len(dp)

    def bisect_left(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left


"""
  [1, 3, 6, 7, 9, 4, 10, 5, 6]
               i 

   1. 2. 3. 4. 5. 3. 6.  3. 5

if nums[j] > nums[i]:
    dp[j] = max(dp[i] + 1, dp[j])
else:


"""







