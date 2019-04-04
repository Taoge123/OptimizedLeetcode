
"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
"""

"""
Approach #2: Sliding Window [Accepted]
Intuition

For each right, call opt(right) the smallest left so that the product of the 
subarray nums[left] * nums[left + 1] * ... * nums[right] is less than k. 
opt is a monotone increasing function, so we can use a sliding window.

Algorithm

Our loop invariant is that left is the smallest value 
so that the product in the window prod = nums[left] * nums[left + 1] * ... * nums[right] is less than k.

For every right, we update left and prod to maintain this invariant. 
Then, the number of intervals with subarray product less than k and with right-most coordinate right, 
is right - left + 1. We'll count all of these for each value of right.
"""

class Solution1:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

"""
Subarray Product Less Than K https://leetcode.com/problems/subarray-product-less-than-k/description/

Two Pointer Solution

Initialize start and end to index 0. Initialize prod to 1. Iterate end from 0 to len(nums)-1. 
Now if prod * nums[end] is less than k, then all subarray between start and end contribute to the solution. 
Since we are moving from left to right, we would have already counted all valid subarrays from start to end-1. 
How many new subarrays with nums[end]? Answer: end-start+1. What will be the updated prod? Answer: prod * nums[end].
What if prod * nums[end] >= k? We need to contract the subarray by advancing start until we get a valid solution again. 
Now what do we do when start > end? Answer: prod=1.
Special case: k=0.
Time is O(N) and space is O(1).
Issue: Overflow with multiplication.
"""

class Solution2:
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0:
            return 0
        start, prod, cnt = 0, 1, 0
        for end in range(len(nums)):
            while start <= end and prod*nums[end] >= k:
                prod = prod/nums[start]
                start += 1
            prod = 1 if start > end else prod*nums[end]
            cnt = cnt if start > end else cnt+(end-start+1)
        return cnt



