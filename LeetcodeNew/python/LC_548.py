"""
Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.
Example:
Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5.
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
Note:
1 <= n <= 2000.
Elements in the given array will be in range [-1,000,000, 1,000,000].
"""

import collections

class Solution:
    def splitArray(self, nums):
        dp = [0]
        for num in nums:
            dp.append(dp[-1] + num)

        N = len(nums)
        visited = collections.defaultdict(list)
        for i, val in enumerate(dp):
            visited[val].append(i)

        for j in range(1, N-1):
            for k in range(j+1, N-1):
                for i in visited[dp[-1] - dp[k+1]]:
                    if i >= j:
                        break
                    if dp[i] == dp[j] - dp[i+1] == dp[k] - dp[j+1]:
                        return True
        return False


class Solution2:
    def splitArray(self, nums) -> bool:

        if len(nums) < 7:
            return False

        n = len(nums)
        dp = [nums[0]]

        for i in range(1, n):
            dp.append(dp[-1] + nums[i])

        for j in range(3, n - 3):
            res = set()
            for i in range(1, j - 1):
                if dp[i - 1] == dp[j - 1] - dp[i]:
                    res.add(dp[i - 1])

            for k in range(j + 2, n - 1):
                if dp[n - 1] - dp[k] == dp[k - 1] - dp[j] and (dp[k - 1] - dp[j]) in res:
                    return True

        return False



class Solution3:
    def splitArray(self, nums):
        temp = 0
        for i, num in enumerate(nums):
            if num == 0:
                continue
            temp += num
            if self.dfs(3, nums[i + 2:], temp, {}):
                return True
        return False

    def dfs(self, parts, nums, target, memo):
        if not nums:
            return False
        if parts == 1:
            return sum(nums) == target
        elif len(nums) <= parts:
            return False
        temp = 0
        for i, num in enumerate(nums):
            temp += num
            if temp == target:
                if self.dfs(parts - 1, nums[i + 2:], target, memo):
                    return True
        return False




nums = [1,2,1,2,1,2,1]
a = Solution()
print(a.splitArray(nums))



