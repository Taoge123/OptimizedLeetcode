"""
673.Number-of-Longest-Increasing-Subsequence
在传统的LIS的DP解法基础上，再设置一个表征LIS数目的数组。len[i]表示以i元素结尾的LIS的长度；num[i]表示以i元素结尾的LIS的数目。

递推关系是：

len[i] = max (len[j]+1) for 0<=j<i && nums[j]<nums[i]

num[i] = sum (num[j]) for 0<=j<i && len[j]+1=len[i]
"""

import collections
import bisect


class Solution:
    def findNumberOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        length = [1] * len(nums)
        count = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                if length[j] + 1 > length[i]:
                    length[i] = max(length[i], length[j] + 1)
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]

        maxLen = max(length)
        return sum(count[i] for i in range(len(count)) if length[i] == maxLen)



class SolutionFast:
    def findNumberOfLIS(self, nums):
        dp = collections.defaultdict(collections.Counter)
        dp[-1][-1e9] = 1
        table = []
        for i in nums:
            index = bisect.bisect_left(table, i)
            if index == len(table):
                table.append(i)
            else:
                table[index] = i
            dp[index][i] += sum(dp[index-1][j] for j in dp[index-1] if j < i)
        return sum(dp[max(0, len(table)-1)].values())






