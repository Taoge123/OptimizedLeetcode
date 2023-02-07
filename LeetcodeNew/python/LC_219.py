"""
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):

        table = {}

        for i, num in enumerate(nums):
            if num in table and i - table[num] <= k:
                return True
            table[num] = i
        return False


class SolutionTony:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        n = len(nums)
        left = 0
        for right in range(1, n):
            while right - left > k:
                left += 1
            # need to check all of the value between them, so it will TLE
            for k in range(left, right):
                if nums[k] == nums[right]:
                    return True
        return False


class SolutionIncorrect:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        if k == 0:
            if len(set(nums)) == len(nums):
                return True
            else:
                return False
        n = len(nums)
        left = 0
        for right in range(1, n):
            while right - left > k:
                left += 1
            # need to check all of the value between them, so it's not correct
            if nums[left] == nums[right]:
                return True

        return False



nums = [0,1,2,3,2,5]
k = 3
a = SolutionTony()
print(a.containsNearbyDuplicate(nums, k))
