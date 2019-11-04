
"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid.
Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.



Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below,
the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)


Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""



    
    
# First, the 6lines final 1-dimentsional DP version as attached.
class Solution2:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0]) if dungeon else 0
        dp = [float('inf')] * (n-1) + [1]
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                dp[j] = max(1, min(dp[j:j+2]) - dungeon[i][j])
        return dp[0]


"""
Okay, now let me share my thinking process and hope it can help someone who is still struggling with this problem. 
(I'm just a guy who started to learn CS myself several months ago, so any comments are welcome!)

When I saw this problem, BFS came to my mind first. Since we can only move downward or rightward at each step,
it's pretty clear what we have is a directional graph. But wait a second, in order to keep the efficiency, 
we'd better have a memo (dictionary in Python) and it needs some extra space and syntax. Do we have a better way?

The answer is YES and let's do DP instead. Build 2-dimensional DP is pretty straight forward. 
We build a matrix called dp whose size is exactly the same as dungeon. 
Since what we want is the minimum hp we need at the starting point dp[0][0] 
and our destination is dp[m-1][n-1], let's update our dp[i][j] from bottom right. 
Attached is my first 2-dimensional DP version.
"""
class Solution3:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0]) if dungeon else 0
        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                dp[i][j] = max(1, min([dp[x][y] for x, y in ((i+1, j), (i, j+1)) \
                               if x < m and y < n] or [1]) - dungeon[i][j])
        return dp[0][0]



"""
Since I'm only using dp[i+1][j] and dp[i][j+1] to calculate dp[i][j], 
I realized we can transform the 2-dimensional DP to 1-dimensional version 
and the corresponding space complexity drops from O(mn) to O(n). 
Attached is the 1-d O(n) DP. Instead of storing O(mn) dp, 
we only need dp for current row and the previous result pre we just got. Thus, O(n) space achieved.
"""

class Solution4:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0]) if dungeon else 0
        dp, pre = [1] * n, [0] * n
        neigh = []
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                neigh = dp[j+1:j+2] if i == m-1 else pre[j:j+1] + dp[j+1:j+2]
                dp[j] = max(1, min(neigh or [1]) - dungeon[i][j])
            pre[:] = dp[:]
        return dp[0]

"""
Can we do better? Yes we can. After a little observation, I realized that we don't even need pre. 
Because dp[i] == pre[i] indeed! Finally I got the final 1-dimensional DP version on the top of this post. 
(Of course I made some adjustment to the initial condition for dp to make the code more concise.) 
And that's all my thinking process for this problem, hope it can help and any comments are welcome!

EDIT: I just found my idol @StefanPochmann has a post here and my final version DP is almost the same as his. Haha, I'm so excited!

"""


"""
We can use dp[i][j] to store the minimal health we need at dungeon[i][j]. 
And knight needs at least 1 health wherever it is.
Since knight should either go right or down, dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1).
To avoid special handle for border cell, I introduce a pivot row and column at bottom and rightmost in my dp array. 
The cells are filled with inf so knight will never choose to go to there. 
While I set right-bottom corner cells to 1s, indicating knight should eventully pass dungeon[-1][-1] with at least health 1. That's our recurrence base.
So after recurrence, dp[0][0] will have the minimal health knight needs to walk to princess.
"""

class Solution5:
    def calculateMinimumHP(dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0]*n + [float('inf')] for _ in range(m)] + [[float('inf')]*(n-1)+[1,1]]
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        return dp[0][0]


class Solution1:
    # O(m*n) space
    def calculateMinimumHP1(self, dungeon):
        if not dungeon:
            return
        r, c = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for i in range(c - 2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i + 1] - dungeon[-1][i])
        for i in range(r - 2, -1, -1):
            dp[i][-1] = max(1, dp[i + 1][-1] - dungeon[i][-1])
        for i in range(r - 2, -1, -1):
            for j in range(c - 2, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0]

    # O(n) space
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return
        r, c = len(dungeon), len(dungeon[0])
        dp = [0 for _ in range(c)]
        dp[-1] = max(1, 1 - dungeon[-1][-1])
        for i in range(c - 2, -1, -1):
            dp[i] = max(1, dp[i + 1] - dungeon[-1][i])
        for i in range(r - 2, -1, -1):
            dp[-1] = max(1, dp[-1] - dungeon[i][-1])
            for j in range(c - 2, -1, -1):
                dp[j] = max(1, min(dp[j], dp[j + 1]) - dungeon[i][j])
        return dp[0]

    def calculateMinimumHP3(self, dungeon):
        if not dungeon:
            return
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for j in range(n - 2):
            dp[-1][j] = max(dp[-1][j + 1] - dungeon[-1][j], 1)
        for i in range(m - 2, -1, -1):
            dp[i][-1] = max(dp[i + 1][-1] - dungeon[i][-1], 1)
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        return dp[0][0]


#     def calculateMinimumH

a = Solution1()
print(a.calculateMinimumHP3([[0,0]]))

