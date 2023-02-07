
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

import functools

class SolutionTonyTLE:
    def canJump(self, nums) -> bool:

        n = len(nums)
        @functools.lru_cache(None)
        def dfs(i):
            if i >= n - 1:
                return True
            # if i >= n:
            #     return False
            if nums[i] == 0:
                return False

            for j in range(1, nums[i] + 1):
                if dfs(i + j):
                    return True
            return False

        return dfs(0)


class SolutionWiddom:
    def canJump(self, nums) -> bool:
        far = 0
        for i in range(len(nums)):
            if i > far:
                return False
            far = max(far, i + nums[i])
        return far >= len(nums) - 1




class Solution:
    def canJump(self, nums) -> bool:
        maxi = 0
        n = len(nums)

        for i, num in enumerate(nums):
            if maxi < i:
                return False
            if maxi >= n - 1:
                return True
            maxi = max(i + num, maxi)

class Solution2:
    def canJump(self, nums) -> bool:
        maxi = 0
        i = 0
        while i < len(nums) and i <= maxi:
            maxi = max(i + nums[i], maxi)
            i += 1
        return i == len(nums)




nums = [2,0,0]
a = SolutionTest()
print(a.canJump(nums))




