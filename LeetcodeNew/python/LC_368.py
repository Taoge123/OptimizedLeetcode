
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

"""
1 2 3 4 9 36
          i
    j
if nums[i] % nums[j] == 0:
    dp[i] = dp[j] + 1
    parent[i] = j

"""


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






