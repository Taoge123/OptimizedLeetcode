"""
Given a sorted array of integers nums and integer values a, b and c.
Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
"""


class Solution:
    def sortTransformedArray(self, nums, a: int, b: int, c: int):
        nums = [x*x*a + x*b + c for x in nums]
        res = [0] * len(nums)
        left, right = 0, len(nums) - 1
        index, step = (left, 1) if a < 0 else (right, -1)
        while left <= right:
            if nums[left] * -step > nums[right] * -step:
                res[index] = nums[left]
                left += 1
            else:
                res[index] = nums[right]
                right -=1
            index += step
        return res

# nums = [-4,-2,2,4]
# a = 1
# b = 3
# c = 5
nums = [-4,-2,2,4]
a = -1
b = 3
c = 5
obj = Solution()
print(obj.sortTransformedArray(nums, a, b, c))
