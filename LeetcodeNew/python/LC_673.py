import collections
import bisect

class Solution:
    def findNumberOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        count = [1] * len(nums)
        dp[0], count[0] = 1, 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                    elif dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
        maxi = max(dp)
        # print(count)
        return sum([count[i] for i in range(len(count)) if dp[i] == maxi])



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






