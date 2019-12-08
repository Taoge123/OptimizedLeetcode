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
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)

        N = len(nums)
        visited = collections.defaultdict(list)
        for i, u in enumerate(preSum):
            visited[u].append(i)

        for j in range(1, N-1):
            for k in range(j+1, N-1):
                for i in visited[preSum[-1] - preSum[k+1]]:
                    if i >= j:
                        break
                    if preSum[i] == preSum[j] - preSum[i+1] == preSum[k] - preSum[j+1]:
                        return True
        return False


nums = [1,2,1,2,1,2,1]
a = Solution()
print(a.splitArray(nums))



