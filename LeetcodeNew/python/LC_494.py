

"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

import collections

class SolutionDP:
    def findTargetSumWays(self, nums, S: int) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 1
        for num in nums:
            newDP = collections.defaultdict(int)
            for prevSum in dp.keys():
                newDP[prevSum + num] += dp[prevSum]
                newDP[prevSum - num] += dp[prevSum]
            dp = newDP
        return dp[S]


class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        memo = {}
        return self.dfs(nums, S, 0, 0, memo)

    def dfs(self, nums, target, pos, summ, memo):
        if (pos, summ) in memo:
            return memo[(pos, summ)]

        if pos == len(nums):
            if target == summ:
                return 1
            else:
                return 0

        plus = self.dfs(nums, target, pos + 1, summ + nums[pos], memo)
        minus = self.dfs(nums, target, pos + 1, summ - nums[pos], memo)
        memo[(pos, summ)] = plus + minus
        return memo[(pos, summ)]


nums = [1, 1, 1, 1, 1]
S = 3
a = Solution2()
print(a.findTargetSumWays(nums, S))

