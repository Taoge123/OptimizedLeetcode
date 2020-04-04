
"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.
"""


class SolutionBruteBorce:
    def maxSubArray(self, nums) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)



class Solution1:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


class Solution2:
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


class Solution3:
    def maxSubArray(self, nums):
        for i in range(1,len(nums)):
            nums[i]=max(nums[i], nums[i]+nums[i-1])
        return max(nums)


class Solution4:
    # DP, O(n) space
    def maxSubArray(self, nums):
        if not nums:
            return None
        dp = [0] * len(nums)
        res = dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res

    # DP, constant space
    def maxSubArray2(self, nums):
        if not nums:
            return None
        loc = glo = nums[0]
        for i in range(1, len(nums)):
            loc = max(loc + nums[i], nums[i])
            glo = max(loc, glo)
        return glo


class Solution5:
    def maxSubArray(self, A):
        current = 0
        result = A[0]
        for i in A:
            current += i
            result = max(current, result)
            current = max(0, current)
        return result


class Solution6:
    def maxSubArray(self, nums):
        sum = res = nums[0]
        for i in range(1, len(nums)):
            sum = max(nums[i], sum + nums[i])
            res = max(res, sum)
        return res

