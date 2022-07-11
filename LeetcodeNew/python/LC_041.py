"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

"""


class SolutionRika:
    def firstMissingPositive(self, nums) -> int:

        # replace all negative num and zero to 1
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # use indexing to check mark down existing num --> num in specific indexing will be marked as negative
        for i in range(n):
            index = abs(nums[i])
            if index <= n:
                nums[index - 1] = -abs(nums[index - 1])

        # for loop each index to see which num are not marked down as negative --> return index
        for index in range(n):  # from small to large
            if nums[index] > 0:
                return index + 1

        return n + 1  # no missing, return n+1


class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1
        for i in range(n):
            if abs(nums[i]) <= n:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


nums = [3,4,-1,1]
a = Solution()
print(a.firstMissingPositive(nums))


