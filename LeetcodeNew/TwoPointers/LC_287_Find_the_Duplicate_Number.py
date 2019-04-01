
"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
"""

class Solution1:
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

class Solution2:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

class Solution3:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1

"""
The idea is quite similar to problem Linked List Cycle II, while it's not easy to figure it out in the beginning:
"""
class Caikehe:
    # fast-slow pointers
    def findDuplicate(self, nums):
        slow = fast = head = len(nums)
        slow = nums[slow - 1]
        fast = nums[nums[fast - 1] - 1]
        while slow != fast:
            slow = nums[slow - 1]
            fast = nums[nums[fast - 1] - 1]
        while head != slow:
            head = nums[head - 1]
            slow = nums[slow - 1]
        return head





