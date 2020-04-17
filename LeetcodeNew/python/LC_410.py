
"""
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

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

"""
410. Split Array Largest Sum
774. Minimize Max Distance to Gas Station
875. Koko Eating Bananas
1011. Capacity To Ship Packages Within D Days
1231. Divide Chocolate
1201. Ugly Number III
"""


class Solution:
    def splitArray(self, nums, m):
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (right - left) // 2 + left
            if self.valid(mid, nums, m):
                right = mid
            else:
                left = mid + 1

        return left

    def valid(self, target, nums, m):
        cuts, total = 0, 0
        for num in nums:
            total += num
            if total > target:
                total = num
                cuts += 1
                if cuts >= m:
                    return False
        return True



class SolutionTony:
    def splitArray(self, nums, m: int) -> int:
        left, right = max(nums), sum(nums) + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.search(nums, mid) <= m:
                right = mid
            else:
                left = mid + 1
        return left

    def search(self, nums, mid):
        count = 1
        curSum = 0
        for num in nums:
            curSum += num
            if curSum > mid:
                count += 1
                curSum = num
        return count





class Solution2:
    def splitArray(self, nums, m: int) -> int:

        n = len(nums)
        summ = [0] * (n + 1)
        dp = [[float('inf') for i in range(n + 1)] for j in range(m + 1)]

        dp[0][0] = 0

        for i in range(1, n + 1):
            summ[i] = summ[i - 1] + nums[i - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(i - 1, j):
                    val = max(dp[i - 1][k], summ[j] - summ[k])
                    dp[i][j] = min(dp[i][j], val)

        return dp[m][n]


nums = [7,2,5,10,8]
m = 2
a = SolutionTest()
print(a.splitArray(nums, m))


