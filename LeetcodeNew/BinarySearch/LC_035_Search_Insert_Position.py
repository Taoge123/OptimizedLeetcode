
"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""
import bisect

class Solution1:
    def searchInsert(self, A, target):
        for i in range(len(A)):
            if target == A[i]:
                return i
            if i == 0 and target < A[i]:
                return 0
            if i != 0 and target < A[i] and target > A[i-1]:
                return i
        return len(A)


class SolutionCaikehe:
    # O(n) time
    def searchInsert1(self, nums, target):
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] < target:
                i += 1
            return i

    # O(lgn) time
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                if target <= nums[l]:
                    return l
                else:
                    return l + 1
            mid = (l + r) >> 1
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid


    # O(lgn) time
    def searchInsert3(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return l


    # O(lgn) time, recursively
    def searchInsert(self, nums, target):
        return self.helper(nums, 0, len(nums) - 1, target)


    def helper(self, nums, l, r, target):
        if l == r:
            if nums[l] >= target:
                return l
            else:
                return l + 1
        mid = l + (r - l) // 2
        if nums[mid] > target:
            return self.helper(nums, l, mid, target)
        elif nums[mid] < target:
            return self.helper(nums, mid + 1, r, target)
        else:
            return mid


class Solution2:
    def searchInsert(self, nums, target):
        nums += [2 * 31 - 1]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if target - 1 < nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l


class Solution3:
    searchInsert = bisect.bisect_left


