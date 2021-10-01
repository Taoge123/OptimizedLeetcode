"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
"""
"""
https://leetcode.com/problems/wiggle-subsequence/discuss/473844/Python-Memoization


"""


import functools

class Solution:
    def wiggleMaxLength(self, nums):
        @functools.lru_cache(None)
        def dfs(i, increase):
            if i >= len(nums):
                return 1  # Found End

            # Search positive, negative, and skip edge cases. On the first iteration, the edge can be neg or pos --> None is valid
            up, down = 0, 0
            if (nums[i] > nums[i - 1] and (increase == False or increase == None)):
                up = 1 + dfs(i + 1, True)
            if (nums[i] < nums[i - 1] and (increase == True or increase == None)):
                down = 1 + dfs(i + 1, False)
            no_change = dfs(i + 1, increase)

            return max(up, down, no_change)

        return dfs(1, None)  # Problem constrains to at least 1


class SolutionTony00:
    def wiggleMaxLength(self, nums):

        memo = {}
        return self.dfs(nums, 1, None, nums[0], memo)

    def dfs(self, nums, i, increase, last, memo):
        if (i, increase) in memo:
            return memo[(i, increase)]

        if i >= len(nums):
            return 1

        up, down = 0, 0
        if (nums[i] > nums[i - 1] and (increase == False or increase == None)):
            up = self.dfs(nums, i + 1, True, nums[i], memo) + 1
        if (nums[i] < nums[i - 1] and (increase == True or increase == None)):
            down = self.dfs(nums, i + 1, False, nums[i], memo) + 1
        no_change = self.dfs(nums, i + 1, increase, last, memo)

        memo[(i, increase)] = max(up, down, no_change)
        return memo[(i, increase)]



class Solution00:
    def wiggleMaxLength(self, nums):

        memo = {}
        return self.dfs(nums, 1, None, memo)

    def dfs(self, nums, i, increase, memo):
        if (i, increase) in memo:
            return memo[(i, increase)]

        if i >= len(nums):
            return 1

        up, down = 0, 0
        if (nums[i] > nums[i - 1] and (increase == False or increase == None)):
            up = self.dfs(nums, i + 1, True, memo) + 1
        if (nums[i] < nums[i - 1] and (increase == True or increase == None)):
            down = self.dfs(nums, i + 1, False, memo) + 1
        no_change = self.dfs(nums, i + 1, increase, memo)

        memo[(i, increase)] = max(up, down, no_change)
        return memo[(i, increase)]


class SolutionTony2:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(i, last, increase):
            if i >= len(nums):
                return 1  # Found End

            # Search positive, negative, and skip edge cases. On the first iteration, the edge can be neg or pos --> None is valid
            up, down = 0, 0
            if (nums[i] > last and (increase == False or increase == None)):
                up = 1 + dfs(i + 1, nums[i], True)
            if (nums[i] < last and (increase == True or increase == None)):
                down = 1 + dfs(i + 1, nums[i], False)
            no_change = dfs(i + 1, last, increase)

            return max(up, down, no_change)

        return dfs(1, nums[0], None)  # Problem constrains to at least 1


class Solution:
    def wiggleMaxLength(self, nums) -> int:

        if not nums:
            return 0
        n = len(nums)
        up = [0] * n
        down = [0] * n
        up[0], down[0] = 1, 1

        for i in range(1, n):
            if nums[i-1] < nums[i]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i-1] > nums[i]:
                up[i] = up[i-1]
                down[i] = up[i-1] + 1
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
        return max(up[-1], down[-1])


class Solution2:
    def wiggleMaxLength(self, nums) -> int:
        if not nums:
            return 0

        up, down = 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i -1]:
                up = down + 1
            elif nums[i] < nums[i -1]:
                down = up + 1
        return max(up, down)


# nums = [1,2,3,4,5,6,7,8,9]
nums = [1,3,1,4,5,2,1]

a = Solution2()
print(a.wiggleMaxLength(nums))







