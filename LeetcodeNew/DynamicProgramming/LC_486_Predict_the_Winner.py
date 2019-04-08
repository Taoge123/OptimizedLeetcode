
"""
Given an array of scores that are non-negative integers.
Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on.
Each time a player picks a number, that number will not be available for the next player.
This continues until all the scores have been chosen. The player with the maximum score wins.

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
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7.
No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
"""

from functools import lru_cache

class Solution1:
    def PredictTheWinner(self, nums):
        memo = {}

        def helper(_sum, nums, start, end):

            if (start, end) in memo:
                return memo[(start, end)]

            if start == end:
                memo[(start, end)] = nums[start]
                return nums[start]

            score1 = _sum - helper(_sum - nums[start], nums, start + 1, end)
            score2 = _sum - helper(_sum - nums[end], nums, start, end - 1)

            res = max(score1, score2)
            memo[(start, end)] = res

            return res

        return helper(sum(nums), nums, 0, len(nums) - 1) * 2 >= sum(nums)


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

"""
we just want to compute the cost, we can assume that player1 pick the number we add it to the dp array, 
\and player2 pick we minus it
and dp represent the area of numbers(dp[0][n-1] represent the final) we need to make the cost minimum
so we use dp[i][j] = max(nums[j] - dp[i][j-1],nums[i] - dp[i+1][j])
"""
class Solution2:
    def PredictTheWinner(self, nums):

        n = len(nums)
        if n == 1 or n%2==0 : return True
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                dp[i][j] = max(nums[j] - dp[i][j-1],nums[i] - dp[i+1][j])
        return dp[0][-1]>=0


"""
Keep track of the difference between player1 and player2. Return True if the difference >= 0 (player1 >= player2)
"""
class Solution3:
    def PredictTheWinner(self, nums):

        dp = {}

        def find(i, j):
            if (i, j) not in dp:
                if i == j:
                    return nums[i]
                dp[i,j] = max(nums[i]-find(i+1, j), nums[j]-find(i, j-1))
            return dp[i,j]

        return find(0, len(nums)-1) >= 0

"""
When a player deals with a[0], a[1], a[2], ... a[n-1], 
the player chooses either a[0] or a[n-1], leaving [a[1], ..., a[n-1]] or [a[0], ..., a[n-2]], resp.

So whether the player can win depends on the results of the above two cases. 
Let w[0][n-1] be the maximum difference between the scores of the player 
and the opponent with start index 0 and end index n-1, then in the two cases, 
the maximum differences that the player can achieve are a[0] - w[1][n-1], a[n-1]-w[0][n-2].

We can further reduce the space complexity by compressing w to one demension, as the following code shows.
"""
class Solution4:
    def PredictTheWinner(self, nums):

        n = len(nums)
        w = [nums[i] for i in range(n)]
        for gap in range(1, n):
            for start in range(n-gap):
                w[start] = max(nums[start]-w[start+1], nums[start+gap]-w[start])
        return w[0] >= 0


"""
Here are my 7 python solutions.

They are:

Naive solution
Recursion without cache by determining whether it's a winner or loser
Advanced solutions
Recursion with cache by calculating the score
Recursion with cache by calculating the score difference
Dp bottom-up, space O(N^2) by calculating the score
Dp bottom-up, space O(N^2) by calculating the score difference
Best solutions
Dp bottom-up, space O(N) by calculating score
Dp bottom-up, space O(N) by calculating the score difference
And the trick mentioned in the title is:

We can simply return True.

This problem is a generalization of 877. Stone Game .
The answer is True when our input length is even and sum of them is odd.

With this and dp (see the bottom), we can reach runtime: 36 ms, 
faster than 96.38% of Python3 online submissions for Predict the Winner even nowadays ( 2019/03/21).
"""

"""
Naive Solution
Recursion without cache by determining whether it's winner or loser
"""


class Solution11:
    def PredictTheWinner(self, nums):
        left, right = 0, 1
        p1 = p2 = 0  # Player scores.
        turn = 0  # 0 for player 1's turn, 1 for player 2's.

        def choose(side, arr, turn, p1, p2):
            if not arr:
                return p1 >= p2 if turn == 0 else p1 < p2

            score = arr[0] if side == left else arr[-1]
            arr = arr[1:] if side == left else arr[:-1]
            if turn == 0:
                p1 += score
            else:
                p2 += score
            turn = (turn + 1) % 2
            return not choose(left, arr, turn, p1, p2) and not choose(right, arr, turn, p1, p2)

        return choose(left, nums, turn, p1, p2) or choose(right, nums, turn, p1, p2)


"""
Advanced Solutions
Recursion with cache by calculating the score
"""

import functools


class Solution22:
    def PredictTheWinner(self, nums):

        @lru_cache(maxsize=None)
        def total(i, j):
            """Returns the total score in the region from i to j."""
            if j - i == 1:
                return nums[i]
            return total(i, j - 1) + nums[j - 1]

        @lru_cache(None)
        def score(i, j):
            if j - i == 1:
                return nums[i]
            return total(i, j) - min(score(i + 1, j), score(i, j - 1))

        return score(0, len(nums)) >= sum(nums) / 2


"""
Recursion with cache by calculating the score difference
"""


class Solution33:
    def PredictTheWinner(self, nums):
        @lru_cache(maxsize=None)
        def score_diff(i, j):
            """Returns the score of player 1 minus that of player 2."""

            if j - i == 1:
                return nums[i]

            left = nums[i] - score_diff(i + 1, j)
            right = nums[j - 1] - score_diff(i, j - 1)
            return max(left, right)

        return score_diff(0, len(nums)) >= 0

"""
Dp bottom-up, space O(N^2) by calculating the score
"""


class Solution44:
    def PredictTheWinner(self, nums):
        n = len(nums)
        score = [[0] * n for __ in range(n)]
        total = [[0] * n for __ in range(n)]
        for x in range(n):
            score[x][x] = total[x][x] = nums[x]

        for length in range(2, n + 1):
            for i in range(n + 1 - length):
                j = i + length - 1
                total[i][j] = total[i][j - 1] + nums[j]  # Total score in region from i to j.
                score[i][j] = total[i][j] - min(score[i + 1][j], score[i][j - 1])

        return score[0][n - 1] >= sum(nums) / 2


"""
Dp bottom-up, space O(N^2) by calculating the score difference
"""


class Solution55:
    def PredictTheWinner(self, nums):
        n = len(nums)
        score_diff = [[0] * n for __ in range(n)]
        for x in range(n):
            score_diff[x][x] = nums[x]

        for length in range(2, n + 1):
            for i in range(n + 1 - length):
                j = i + length - 1
                left = nums[i] - score_diff[i + 1][j]
                right = nums[j] - score_diff[i][j - 1]
                score_diff[i][j] = max(left, right)

        return score_diff[0][n - 1] >= 0


"""
Best Solutions
Dp bottom-up, space O(N) by calculating the score
"""


class Solution66:
    def PredictTheWinner(self, nums):
        n = len(nums)
        score = [num for num in nums]
        total = [num for num in nums]

        for length in range(2, n + 1):
            for i in range(n + 1 - length):
                j = i + length - 1
                total[i] += nums[j]  # Total score in region from i to j.
                score[i] = total[i][j] - min(score[i + 1], score[i])

        return score[0] >= sum(nums) / 2


"""
Dp bottom-up, space O(N) by calculating the score difference
"""
class Solution77:
    def PredictTheWinner(self, nums):
        n = len(nums)
        score_diff = [num for num in nums]
        for length in range(2, n + 1):
            for i in range(n + 1 - length):
                j = i + length - 1
                left = nums[i] - score_diff[i + 1]
                right = nums[j] - score_diff[i]
                score_diff[i] = max(left, right)
        return score_diff[0] >= 0


"""
With the Trick
"""


class Solution88:
    def PredictTheWinner(self, nums):
        n = len(nums)
        if n % 2 == 0 and sum(nums) % 2 == 1:
            return True

        score_diff = [num for num in nums]
        for length in range(2, n + 1):
            for i in range(n + 1 - length):
                j = i + length - 1
                left = nums[i] - score_diff[i + 1]
                right = nums[j] - score_diff[i]
                score_diff[i] = max(left, right)
        return score_diff[0] >= 0

