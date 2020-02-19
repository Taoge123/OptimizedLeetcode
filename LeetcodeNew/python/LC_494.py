

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

class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        cache = {}
        return self.helper(nums, 0, S, cache)

    def helper(self, nums, pos, target, cache):
        if (pos, target) in cache:
            return cache[(pos, target)]

        else:
            res = 0
            if pos == len(nums):
                if target == 0:
                    res = 1

            else:
                add = self.helper(nums, pos + 1, target + nums[pos], cache)
                minus = self.helper(nums, pos + 1, target - nums[pos], cache)
                res = add + minus
            cache[(pos, target)] = res
        return cache[(pos, target)]




class Solution2:
    def findTargetSumWays(self, nums, S: int) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 1
        for num in nums:
            step = collections.defaultdict(int)
            for prevSum in dp.keys():
                step[prevSum + num] += dp[prevSum]
                step[prevSum - num] += dp[prevSum]
            dp = step
        return dp[S]




nums = [1, 1, 1, 1, 1]
S = 3
a = Solution2()
print(a.findTargetSumWays(nums, S))

