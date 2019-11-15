
"""
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
        print(dp)
        print(parent)
        while index != -1:
            res.append(nums[index])
            index = parent[index]
        return res






