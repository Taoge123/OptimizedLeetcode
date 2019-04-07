
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?

"""

class SolutionLee:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) >> 1
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r = r - 1
        return nums[l]

# Find Minimum in Rotated Sorted Array I----no duplicate ----O(logN)
class Solution2:
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi -lo) / 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


# Find Minimum in Rotated Sorted Array II----contain duplicates----O(logN)~O(N)

class Solution3:
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi -lo) / 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid if nums[hi] != nums[mid] else hi - 1
        return nums[lo]


class Solution4:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        left, right = 0, len(num) - 1

        while (right - left) > 1:
            mid = (left + right) >> 1
            if num[mid] > num[left] and num[mid] > num[right]:
                left = mid
            elif num[mid] == num[left]:  #we can get AC of it's previous question if we remove this condition
                left += 1
            else:
                right = mid

        return min(num[left], num[right])




