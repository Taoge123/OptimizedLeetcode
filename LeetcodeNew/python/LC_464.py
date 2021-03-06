

"""
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
"""


class Solution:
    def canIWin(self, num: int, target: int) -> bool:
        if num * (num + 1) // 2 < target:
            return False
        cache = {}
        return self.helper(tuple(range(1, num + 1)), target, cache)

    def helper(self, nums, target, cache):
        if not nums:
            return False
        if nums[-1] >= target:
            return True
        if nums in cache:
            return cache[nums]

        for i in range(len(nums)):
            if not self.helper(nums[:i] + nums[i + 1:], target - nums[i], cache):
                cache[nums] = True
                return True
        cache[nums] = False
        return False


class SolutionTony:
    def canIWin(self, n: int, target: int) -> bool:
        if n * (n + 1) // 2 < target:
            return False
        memo = {}
        nums = [i for i in range(1, n + 1)]
        return self.dfs(nums, target, memo)

    def dfs(self, nums, target, memo):
        if tuple(nums) in memo:
            return memo[tuple(nums)]

        if not nums:
            return False

        if nums[-1] >= target:
            return True

        for i in range(len(nums)):
            if not self.dfs(nums[:i] + nums[i + 1:], target - nums[i], memo):
                memo[tuple(nums)] = True
                return memo[tuple(nums)]

        memo[tuple(nums)] = False
        return memo[tuple(nums)]

