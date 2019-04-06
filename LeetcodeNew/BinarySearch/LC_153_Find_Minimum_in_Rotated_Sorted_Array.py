
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""

class Solution1:
    def findMin(self, nums):
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]

        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) / 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1


class Solution2:
    def findMin(self, nums):

        i = 0
        j = len(nums) - 1
        while i < j:
            m = i + (j - i) // 2
            if nums[m] > nums[j]:
                i = m + 1
            else:
                j = m
        return nums[i]

class Solution3:
    def findMin(self, nums):

        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high) // 2
            if low == high:
                return nums[mid]
            if nums[mid] < nums[-1]:
                high = mid
            elif nums[mid] > nums[-1]:
                low = mid + 1


class SolutionCaikehe:

    # Recursively
    def findMin(self, nums):
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = l + (r-l)//2
        if nums[mid] > nums[r]:
            return self.helper(nums, mid+1, r)
        else:
            return self.helper(nums, l, mid)




