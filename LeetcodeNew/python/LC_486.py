
"""
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return False.
Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
"""

"""
For play-chess problem, we track state of the 1st player only and count the 2nd player's decision as influence.
The state is the maximum score the 1st player can get in the current situation (with choosable nums[i] and nums[j]).
The state function is state(i, j)
The goal state we judge if state(0, n-1) is bigger than scoreSum - state(0, n-1), if it is, the 1st will win.
state transition:
Let's build the search tree first, take nums = [3, 2, 4] for example,

 [3,2,4]
   3/\4---------- 1st player's decision
[2,4] [3,2]
2/ \4  3/ \2----- 2nd player's decision
[4][2] [2][3]

currently 1st with choosable i, j,
        1.if 1st picks nums[i], 2nd can pick either ends of nums[i + 1, j]
            a.if 2nd picks nums[i + 1], 1st can pick either ends of nums[i + 2, j]
            b.if 2nd picks nums[j], 1st can pick either ends of nums[i + 1, j - 1]
            since 2nd plays to maximize his score, 1st can get nums[i] + min(1.a, 1.b)
						
        2.if 1st picks nums[j], Lee can pick either ends of nums[i, j - 1]
            a.if 2nd picks nums[i], 1st can pick either ends of nums[i + 1, j - 1];
            b.if 2nd picks nums[j - 1], 1st can pick either ends of nums[i, j - 2];
            since 2nd plays to maximize his score, 1st can get nums[j] + min(2.a, 2.b)
        
        since the 1st plays to maximize his score, 1st can get max(nums[i] + min(1.a, 1.b), nums[j] + min(2.a, 2.b));
"""


class SolutionSlow:
    def PredictTheWinner(self, nums) -> bool:
        return self.dfs(nums, 0, len(nums) - 1) >= 0

    def dfs(self, nums, i, j):
        if i == j:
            return nums[i]
        x = self.dfs(nums, i + 1, j)
        y = self.dfs(nums, i, j - 1)

        return max(nums[i] - x, nums[j] - y)


class Solution:
    def PredictTheWinner(self, nums) -> bool:

        memo = {}
        return self.dfs(nums, 0, len(nums) - 1, memo) >= 0

    def dfs(self, nums, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == j:
            return nums[i]

        memo[(i, j)] = max(nums[i] - self.dfs(nums, i + 1, j, memo), nums[j] - self.dfs(nums, i, j - 1, memo))
        return memo[(i, j)]


class Solution2:
    def PredictTheWinner(self, nums):
        n = len(nums)
        memo = [[-1 for _ in range(n)] for _ in range(n)]
        scoreFirst = self.helper(nums, 0, n - 1, memo)
        scoreTotal = sum(nums)
        return scoreFirst >= scoreTotal - scoreFirst

    def helper(self, nums, i, j, memo):
        # Base case.
        if i > j:
            return 0
        if i == j:
            return nums[i]
        if memo[i][j] != -1:
            return memo[i][j]
        # Recursive case.
        score = max(nums[i] + min(self.helper(nums, i + 2, j, memo), self.helper(nums, i + 1, j - 1, memo)),
                       nums[j] + min(self.helper(nums, i, j - 2, memo), self.helper(nums, i + 1, j - 1, memo)))
        memo[i][j] = score
        return score




class SolutionTony:
    def PredictTheWinner(self, nums) -> bool:
        memo = {}
        score = self.dfs(nums, 0, len(nums) - 1, memo)
        return score >= sum(nums) - score

    def dfs(self, nums, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        if i == j:
            return nums[i]

        left = nums[i] = min(self.dfs(nums, i + 2, j, memo), self.dfs(nums, i + 1, j - 1, memo))
        right = nums[j] + min(self.dfs(nums, i, j - 2, memo), self.dfs(nums, i + 1, j - 1, memo))
        memo[(i, j)] = max(left, right)
        return memo[(i, j)]



