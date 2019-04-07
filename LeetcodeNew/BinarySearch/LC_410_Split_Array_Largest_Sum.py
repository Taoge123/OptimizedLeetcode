
"""
https://leetcode.com/problems/split-array-largest-sum/discuss/89846/Python-solution-with-detailed-explanation
https://leetcode.com/problems/split-array-largest-sum/discuss/89819/c-fast-very-clear-explanation-clean-code-solution-with-greedy-algorithm-and-binary-search
https://leetcode.com/problems/split-array-largest-sum/discuss/89817/Clear-Explanation:-8ms-Binary-Search-Java

Given an array which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18."""

"""
解题思路：
二分枚举答案（Binary Search）

将数组nums拆分成m个子数组，每个子数组的和不小于sum(nums) / m，不大于sum(nums)

又因为数组nums中只包含非负整数，因此可以通过二分法在上下界内枚举答案。

时间复杂度O(n * log m)，其中n是数组nums的长度，m为数组nums的和
"""
"""
First i try dp, while got TLE:(while if using java to implement dp, u may get AC...)
"""
import sys
class Solution1:
    def splitArray(self, nums, m):

        dp = [[float('inf') for j in range(m+1)] for i in range(len(nums)+1)]
        dp[0][0] = 0
        sub = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            sub[i+1] = sub[i] + nums[i]
        for i in range(1, len(nums)+1):
            for j in range(1, m+1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], sub[i]-sub[k]))
        return dp[len(nums)][m]

"""
The m dimension can be optimized because new [j] value only depends on [j - 1], 
so a 1-D dp array is enough for this problem.
Note that the calculaiton sequence for i is from large to small, 
because calculate new f[i] will use old f[k] values in which k < i.
"""
class Solution2:
    def splitArray(self, nums, m):
        if not nums or not m or len(nums) < m:
            return

        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]

        f = [float("inf")] * (n + 1)
        f[0] = 0

        for j in range(m):
            for i in range(n, 0, -1):  # must be from n to 1, otherwise results will be wrong
                for k in range(j - 1, i):
                    f[i] = min(f[i], max(f[k], presum[i] - presum[k]))

        return f[n]

# Then by binary search, got AC:
class Solution3:
    def splitArray(self, nums, m):

        def valid(mid):
            cnt = 0
            current = 0
            for n in nums:
                current += n
                if current>mid:
                    cnt += 1
                    if cnt>=m:
                        return False
                    current = n
            return True

        l = max(nums)
        h = sum(nums)

        while l<h:
            mid = l+(h-l)/2
            if valid(mid):
                h = mid
            else:
                l = mid+1
        return l



class Solution:
    def check(self, nums, m, max_sum):
        """Returns whether it is possible to split nums into m arrays with maximum subarray sum <= max_sum
        """
        assert m <= len(nums)

        min_interval_count = 0
        running = 0
        for i in nums + [float('inf')]:
            if running + i > max_sum:
                min_interval_count += 1
                running = 0
            running += i
        return min_interval_count <= m

    def splitArray(self, nums, m):
        if m > len(nums):
            return False

        lo = max(nums) - 1  # Invariant: self.check always false
        hi = sum(nums)      # Invariant: self.check always true

        # Binary search: move lo and hi towards each other, until they meet
        while lo != hi - 1:
            mid = (lo + hi) // 2
            if self.check(nums, m, mid):
                hi = mid
            else:
                lo = mid

        return hi





