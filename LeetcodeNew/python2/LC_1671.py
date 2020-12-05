"""
similar to LIS
consider nums[i] as peak
array length = leftLIS[i] + rightLIS[i] - 1

n ^ 2
X X X X X i X X X

dp[i] = max(dp[j] + 1)  for all nums[j] < nums[i]

n * log(n)
maintain a increasing stack

nums = 1 3 5 7



"""


class Solution:
    def minimumMountainRemovals(self, nums) -> int:

        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    left[i] = max(left[i], left[j] + 1)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    right[i] = max(right[i], right[j] + 1)

        maxLen = 0
        for i in range(n):
            if left[i] >= 2 and right[i] >= 2:
                maxLen = max(maxLen, left[i] + right[i] - 1)

        return n - maxLen



class SolutionLIS:
    def minimumMountainRemovals(self, nums) -> int:
        left = self.lis(nums)
        right = self.lis(nums[::-1])

        maxLen = 0
        n = len(nums)
        for i in range(n):
            if left[i] >= 2 and right[n - 1 - i] >= 2:
                maxLen = max(maxLen, left[i] + right[n - 1 - i] - 1)

        return n - maxLen

    def lis(self, arr):
        dp = []
        res = []
        for i in range(len(arr)):
            idx = bisect.bisect_left(dp, arr[i])
            if idx >= 0 and idx < len(dp):
                dp[idx] = arr[i]
                res.append(idx + 1)
            else:
                dp.append(arr[i])
                res.append(len(dp))

        return res




