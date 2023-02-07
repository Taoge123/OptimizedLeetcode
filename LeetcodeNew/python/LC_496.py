

"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""

"""
{1: 3, 3: 4, 2: 5, 4: 5}
"""


class SolutionTonnie:
    def nextGreaterElement(self, nums1, nums2):
        table = {}
        stack = []

        # build table based on nums2
        for num in nums2:
            while stack and stack[-1] < num:
                table[stack.pop()] = num
            stack.append(num)

        res = []
        # loop nums1 and get all relationships from table
        for num in nums1:
            if num in table:
                res.append(table[num])
            else:
                res.append(-1)
        return res



class SolutionTony:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        table = {}
        for i, num in enumerate(nums2):
            while stack and stack[-1] < num:
                table[stack.pop()] = num
            stack.append(num)

        res = []
        for num in nums1:
            res.append(table.get(num, -1))
        return res



class Solution:
    def nextGreaterElement(self, nums1, nums2):

        table = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                table[stack.pop()] = num
            stack.append(num)

        res = [table.get(num, -1) for num in nums1]
        return res



num1 = [4,1,2]
num2 = [1,3,4,2,5]
a = Solution()
print(a.nextGreaterElement(num1, num2))


