"""
416. Partition Equal Subset Sum
473. Matchsticks to Square
698. Partition to K Equal Sum Subsets
996. Number of Squareful Arrays
"""
"""
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.
"""


class Solution:
    def makesquare(self, nums):
        if not nums:
            return False
        nums = sorted(nums, reverse=True)
        sumn = sum(nums)
        if sumn % 4:
            return False
        return self.dfs(nums, [0, 0, 0, 0], 0, sumn / 4)

    def dfs(self, nums, res, pos, target):
        if pos == len(nums):
            if res[0] == res[1] == res[2]:
                return True
            return False

        for i in range(4):
            if res[i] + nums[pos] > target:
                continue
            res[i] += nums[pos]
            if self.dfs(nums, res, pos + 1, target):
                return True
            res[i] -= nums[pos]

        return False






class SolutionTony:
    def makesquare(self, nums) -> bool:
        if not nums:
            return False
        nums.sort(reverse=True)
        summ = sum(nums)
        if summ % 4:
            return False

        target = summ // 4
        res = [0] * 4
        memo = {}
        return self.dfs(nums, 0, 0, target, res, memo)

    def dfs(self, nums, pos, cur, target, res, memo):
        if (pos, tuple(res)) in memo:
            return memo[(pos, tuple(res))]

        if pos == len(nums):
            if res[-1] == res[-2] == res[-3]:
                return True
            return False

        for i in range(4):
            if res[i] + nums[pos] > target:
                continue
            res[i] += nums[pos]
            if self.dfs(nums, pos + 1, cur + nums[i], target, res, memo):
                memo[(pos, tuple(res))] = True
                return memo[(pos, tuple(res))]
            res[i] -= nums[pos]
        memo[(pos, tuple(res))] = False
        return memo[(pos, tuple(res))]



class SolutionOptimized:
    def makesquare(self, nums) -> bool:
        if not nums:
            return False
        nums.sort(reverse=True)
        summ = sum(nums)
        if summ % 4:
            return False
        target = summ // 4
        visited = [False] * len(nums)
        return self.dfs(nums, 0, 0, 1, target, visited)

    def dfs(self, nums, pos, cur, count, target, visited):
        if count == 4:
            return True
        if cur == target:
            return self.dfs(nums, 0, 0, count + 1, target, visited)
        if cur > target:
            return False

        for i in range(pos, len(nums)):
            if visited[i] == True:
                continue
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == False:
                continue

            visited[i] = True
            if (self.dfs(nums, i + 1, cur + nums[i], count, target, visited)):
                return True
            visited[i] = False

        return False



