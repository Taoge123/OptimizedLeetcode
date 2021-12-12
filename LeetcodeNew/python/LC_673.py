"""
673.Number-of-Longest-Increasing-Subsequence
在传统的LIS的DP解法基础上，再设置一个表征LIS数目的数组。len[i]表示以i元素结尾的LIS的长度；num[i]表示以i元素结尾的LIS的数目。

递推关系是：

len[i] = max (len[j]+1) for 0<=j<i && nums[j]<nums[i]

num[i] = sum (num[j]) for 0<=j<i && len[j]+1=len[i]
"""

import collections
import bisect
import functools


class SolutionTony:
    def findNumberOfLIS(self, nums):
        @functools.lru_cache(None)
        def dfs(i):
            max_length = 1
            count = 1

            for j in range(i + 1, n):
                if nums[j] > nums[i]:

                    max_length_j, count_j = dfs(j)
                    if max_length == 1 + max_length_j:
                        count += count_j

                    elif 1 + max_length_j > max_length:
                        count = count_j
                        max_length = 1 + max_length_j

            return [max_length, count]

        n = len(nums)
        max_len, count = 0, 0
        for i in range(n):
            curr_max, curr_count = dfs(i)
            if curr_max == max_len:
                count += curr_count
            elif curr_max > max_len:
                max_len = curr_max
                count = curr_count
        return count



class Solution:
    def findNumberOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        # dp is the length
        dp = [1] * len(nums)
        count = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                if dp[j] + 1 > dp[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    count[i] = count[j]
                elif dp[j] + 1 == dp[i]:
                    count[i] += count[j]

        maxLen = max(dp)
        return sum(count[i] for i in range(len(count)) if dp[i] == maxLen)



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






