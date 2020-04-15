"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution:
    def findDuplicate(self, nums) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            #count how many elements are <= mid
            count = self.count(nums, mid)
            #we have more elements than mid, then duplicates is in left, vice versa
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left

    def count(self, nums, target):
        count = 0
        for num in nums:
            if num <= target:
                count += 1
        return count




class Solution2:
    def findDuplicate(self, nums) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                # Once they are equal, point fast back to origen and restart until they meet again
                fast = 0
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow


