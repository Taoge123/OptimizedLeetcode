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
    def findDuplicate(self, nums):

        left, right = 1, len(nums ) -1


        while left <= right:

            mid = left + (right - left) // 2
            count = 0

            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1

            # If there are more nums less than the mid, then go left
            if count > mid:
                right = mid - 1

            else:
                left = mid + 1

        return left


class Solution2:
    def findDuplicate(self, nums) -> int:

        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

