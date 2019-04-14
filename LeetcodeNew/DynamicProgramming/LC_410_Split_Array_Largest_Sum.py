
"""
https://leetcode.com/problems/split-array-largest-sum/discuss/89846/Python-solution-with-detailed-explanation


Given an array which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

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
where the largest sum among the two subarrays is only 18.
"""


class Solution1:
    def splitArray(self, nums, m):

        dp = [[float('inf') for j in range(m+1)] for i in range(len(nums)+1)]
        dp[0][0] = 0
        #Build prefix Sum array
        sub = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            sub[i+1] = sub[i] + nums[i]

        for i in range(1, len(nums)+1):
            #WE split the array from 1 to m pieces
            for j in range(1, m+1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], sub[i]-sub[k]))
        return dp[len(nums)][m]


"""
The O(n^2m) DP solution to this problem is pretty obvious, 
where the transition function can be written as
dp[i][j] = min{max{dp[k][j-1], subsum(k+1, i)}}, 0 <= k < i
where dp[i][j] is the optimal result for splitting nums[:i+1] into j subarrays. 
And then for each i, j you would require O(n) time to find the k that minimizes dp[i][j], which makes this an overall O(n^2m) algorithm..

The key to reducing time complexity down to O(nm) is the monotonic properties that dp and subsum hold. 
Mathematically I found myself hard to explain this well, but intuitively, 
if the last subarray for dp[i][j] is nums[k], nums[k+1], ..., nums[i], 
then for dp[i][j+1] the last subarray would always be some nums[k+x], ..., nums[i], x>=0, 
because if you were cutting an array evenly into j + 1 continuous subarray, 
the last subarray would always be smaller than it would had been using one less cut. 
So every time you find a k that minimizes dp[i][j] you only need to consider subarray starting from or after k when computing dp[i][j+1].
"""

class Solution2:
    def splitArray(self, nums, m):
        n = len(nums)
        if not n:
            return 0
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
        sub_sum = lambda i, j: pre_sum[j + 1] - pre_sum[i]

        dp = [[0 for _ in range(m + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][1] = pre_sum[i + 1]
            k = 0
            for j in range(2, min(m + 1, i + 2)):
                while k < i - 1 and max(dp[k][j-1], sub_sum(k+1, i)) > max(dp[k+1][j-1], sub_sum(k+2,i)):
                    k += 1
                dp[i][j] = max(dp[k][j - 1], sub_sum(k+1, i))
        return dp[n - 1][m]


