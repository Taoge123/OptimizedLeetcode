class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        res = float('-inf')

        for i in range(len(nums)):
            summ = 0
            for j in range(i, len(nums)):
                summ += nums[j]
                if j - i + 1 >= k:
                    res = max(res, summ / (j - i + 1))
        return res


"""
https://leetcode.com/problems/maximum-average-subarray-ii/discuss/105482/Python-solution-with-detailed-explanation
Binary Search Solution

What is the range for the average value? Clearly, any average will lie between min(nums) and max(nums). So the intuition is to use binary search between this range.
lo is initialized to min(nums). hi is initialized to max(nums). x = mid = (lo+hi)/2
Now we want to solve the sub-problem: Does the array nums have a subarray of length greater than equal to k with average atleast x? If yes, then we can restrict our search to the range [x,hi]. Otherwise, we will search in the range [lo,x].
Can we devise a linear time solution for the problem: Does the array nums have a subarray of length greater than equal to k with average atleast x?
nums[i]+...+nums[j] >= x * (j-i-1). This evaluates to: (nums[i]-x) + (nums[i+1]-x) + ...(nums[j]-x) >=0
The problem is transformed into the following problem: Do we have a sub-array of length greater than k in the transformed array with sum greater than zero?
The above problem can be solved in linear time. Start by finding the sum of first k elements nums[i]-mid. If this sum is greater than zero, then we can return True. Otherwise, say we have the cumulative sum until index j i.e. cum(j) where j >= k. Now say we know the minimum cumulative sum until index i i.e. mcum(i) such that j-i >= k. Then if the cum(j) >= mcum(i), we can return True.

"""


class SolutionBS:
    def check(self, mid, nums, k):
        summ = 0
        for i in range(k):
            summ += nums[i] - mid
        if summ >= 0:
            return True
        prev, mini = 0, 0
        for i in range(k, len(nums)):
            summ += nums[i] - mid
            prev += nums[i - k] - mid
            mini = min(mini, prev)
            if summ >= mini:
                return True
        return False

    def findMaxAverage(self, nums, k):
        left, right = min(nums), max(nums)
        while right - left > 0.000006:
            mid = left + (right - left) / 2
            if self.check(mid, nums, k):
                left = mid
            else:
                right = mid
        return left


