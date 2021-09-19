"""
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

import functools


class Solution0:
    def maxProduct(self, nums) -> int:
        def dfs(i, val):
            if i == len(nums):
                return val
            # 3 choices, Include the current number in the product, start a new product, or end the product
            res = max(val, dfs(i + 1, val * nums[i]), dfs(i + 1, nums[i]))
            return res

        return dfs(1, nums[0])



class Solution00:
    def maxProduct(self, nums) -> int:

        memo = {}
        return self.dfs(nums, 1, nums[0], memo)

    def dfs(self, nums, i, val, memo):
        if (i, val) in memo:
            return memo[(i, val)]

        if i == len(nums):
            return val

        res = max(val, self.dfs(nums, i + 1, val * nums[i], memo), self.dfs(nums, i + 1, nums[i], memo))
        memo[(i, val)] = res
        return res


class Solution:
    def maxProduct(self, nums) -> int:

        @functools.lru_cache(None)
        def dfs(i):
            # if i == len(nums):
            #     return 1, 1

            if i == len(nums):
                return [0, 0]

            x = nums[i]
            y = nums[i] * min(dfs(i + 1))
            z = nums[i] * max(dfs(i + 1))
            return max(x, y, z), min(x, y, z)

        res = float('-inf')
        for i in range(len(nums)):
            res = max(res, dfs(i)[0])
        return res


class SolutionTony:
    def maxProduct(self, nums) -> int:
        res = nums[0]
        mini, maxi = nums[0], nums[0]
        for i in range(1, len(nums)):
            newMax = max(nums[i], maxi * nums[i], mini * nums[i])
            newMin = min(nums[i], maxi * nums[i], mini * nums[i])
            maxi, mini = newMax, newMin
            res = max(res, maxi)
        return res




class Solution:
    def maxProduct(self, nums):
        mini = maxi = res = nums[0]

        for num in nums[1:]:
            temp = maxi
            maxi = max(max(maxi * num, mini * num), num)
            mini = min(min(mini * num, temp * num), num)
            res = max(res, maxi)
        return res



class SolutionTest:
    def maxProduct(self, nums) -> int:

        memo = {}
        print(self.dfs(nums, 0, memo))

    def dfs(self, nums, i, memo):
        if i in memo:
            return memo[i]

        if i == len(nums):
            return [1, 1]

        x = nums[i]
        y = nums[i] * min(self.dfs(nums, i + 1, memo))
        z = nums[i] * max(self.dfs(nums, i + 1, memo))

        res = [max(x, y, z), min(x, y, z)]
        memo[i] = res
        return res

nums = [0,2]
a = SolutionTest()
print(a.maxProduct(nums))