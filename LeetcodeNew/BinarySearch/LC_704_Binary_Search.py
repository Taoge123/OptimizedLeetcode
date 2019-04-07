
"""
Given a sorted (in ascending order) integer array nums of n elements
and a target value, write a function to search target in nums.
If target exists, then return its index, otherwise return -1.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
"""
import bisect

class Solution1:
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1


"""
Is there any particular reason in the second solution that using while l <= r 
instead of while l < r? I cannot think of one case it benefits.



actually it depends on how you set r:

if you set r to len(nums), then you use while l < r. when l == r, the search space becomes empty.
if you set r to len(nums) - 1(inclusive), then you should use while l <= r. when l > r, the search space becomes empty.
because eventually you need the while loop to be terminated with an empty range.

"""
class Solutio2:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1


"""
Without using Python library
"""
class Solution3:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1

"""
Use bisect_left
"""
class Solution4:
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)
        return index if index != len(nums) and nums[index] == target else -1

"""
Use bisect_right
"""
class Solution5:
    def search(self, nums, target):
        index = bisect.bisect_right(nums, target)
        return index-1 if index > 0 and nums[index-1] == target else -1


