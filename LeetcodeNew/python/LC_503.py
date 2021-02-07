
"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""


class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        res = [-1] * len(nums)

        for i in list(range(len(nums))) * 2:
            # print(i)
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res



class SolutionTony:
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack = []
        table = {}
        res = [-1] * n

        for i, num in enumerate(nums + nums):
            i %= n
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res


nums = [3,2,1,4]
a = Solution()
print(a.nextGreaterElements(nums))



