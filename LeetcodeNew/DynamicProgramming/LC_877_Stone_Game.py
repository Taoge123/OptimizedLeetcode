
"""
Leetcode 486

Alex and Lee play a game with piles of stones.
There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.
Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.
This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

Example 1:

Input: [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""


"""
https://blog.csdn.net/androidchanhao/article/details/81271077

Approach 1: Just return true
Alex is first to pick pile.
piles.length is even, and this lead to an interesting fact:
Alex can always pick odd piles or always pick even piles!

For example,
If Alex wants to pick even indexed piles piles[0], piles[2], ....., piles[n-2],
he picks first piles[0], then Lee can pick either piles[1] or piles[n - 1].
Every turn, Alex can always pick even indexed piles and Lee can only pick odd indexed piles.

In the description, we know that sum(piles) is odd.
If sum(piles[even]) > sum(piles[odd]), Alex just picks all evens and wins.
If sum(piles[even]) < sum(piles[odd]), Alex just picks all odds and wins.
So, Alex always defeats Lee in this game.
"""

"""
Approach 2: 2D DP
It's tricky when we have even number of piles of stones. You may not have this condition in an interview.

Follow-up:

What if piles.length can be odd?
What if we want to know exactly the diffenerce of score?
Then we need to solve it with DP.

dp[i][j] means the biggest number of stones you can get more than opponent picking piles in piles[i] ~ piles[j].
You can first pick piles[i] or piles[j].

1. If you pick piles[i], your result will be piles[i] - dp[i + 1][j]
2. If you pick piles[j], your result will be piles[j] - dp[i][j - 1]
So we get:
dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
We start from smaller subarray and then we use that to calculate bigger subarray.

Note that take evens or take odds, it's just an easy strategy to win when the number of stones is even.
It's not the best solution!
I didn't find a tricky solution when the number of stones is odd (maybe there is).

"""

"""
In 1D solution,for every inner loop,dp[i] equals to dp[i][i+d] in 2D solution. So let's make [5,3,4,5] as an example, from the very beginning,
dp[0]=dp[0,0]=5,
dp[1]=dp[1,1]=3,
dp[2]=dp[2,2]=4,
dp[3]=dp[3,3]=5,
for the first outer loop , d=1,i=0,1,2
dp[0]=dp[0,1]=2,
dp[1]=dp[1,2]=1,
dp[2]=dp[2,3=1,
and we can find that dp[3] is not be updated, and the truth is that it will never be used in the left loops.
then when d=2,i=0,1
dp[0]=dp[0,2]=4,
dp[1]=dp[1,3]=4,
and both dp[2] and dp[3] were left behind and will never be used.
then d= 3, i=0
dp[0=dp[0,3]=1,
dp[0] means dp[0][n-1] here.
so @WalkerJG is right, i in 1D means i+d in 2D, but he/she didn't express it clearly.
if you try it in details, in 2D solution, only the upper triangle will be updated,and one diagonal for one loop.

"""
"""
分析：

不妨认为Alex第一次拿的piles[0]，那么剩下的是piles[1:]
Lee拿piles[1]还是piles[-1]不取决于这两个数哪个大，而是拿了某个数之后使得剩下的数中Alex能获得的总数小
若定义firstscore(piles)表示在当前piles数组中，先拿的人最后能获得的总分数，
则alex的分数应该是

max(piles[0]+min(firstscore(piles[1:-1]),firstscore(piles[2:])), piles[-1] + min(firstscore(piles[1:-1]), firstscore(piles[:-2])))

思路：

因为涉及到大量重复计算，所以需要采用记忆化的思想，用一个cache存已经计算过的值
但如果用piles作为key值，所花的时间和空间都太大了，所以改成用下标替代的方法
"""
from functools import lru_cache

class Solution1:
    def stoneGame(self, piles):
        cache = {}

        def firstscore(i, j):
            if i >= j:
                return 0
            if j == i + 1 and j < len(piles):
                return piles[i]
            if (i, j) in cache:
                return cache[i, j]
            res = max(piles[i] + min(firstscore(i + 2, j), firstscore(i + 1, j - 1)),
                      piles[j - 1] + min(firstscore(i + 1, j - 1), firstscore(i, j - 2)))
            cache[i, j] = res
            return res

        Alex = firstscore(0, len(piles))
        Lee = sum(piles) - Alex
        return Alex > Lee



"""
            for (int i = 0; i < p.length - d; i++)
                dp[i] = Math.max(p[i] - dp[i + 1], p[i + d] - dp[i]);
Thanks, what does i + d represent?

i is the left index, d is the interval length , so i + d is the right index..
by the way: d can not be 0, this processing has been done by the for (int i = 0; i < n; i++) dp[i][i] = p[i];

"""

class SolutionLee1:
    def stoneGame(self, p):
        n = len(p)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = p[i]
        for d in range(1, n):
            for i in range(n - d): #i + d == j
                #dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
                dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])
        return dp[0][-1] > 0

class SolutionLee11:
    def stoneGame(self, p):
        n = len(p)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = p[i]
        for d in range(1, n):
            for i in range(n - d): #i + d == j
                j = i + d
                dp[i][j] = max(p[i] - dp[i + 1][j], p[j] - dp[i][j - 1])
        return dp[0][-1] > 0

class SolutionLee2:
    def stoneGame(self, p):
        n = len(p)
        dp = p[:]
        for d in range(1, n):
            for i in range(n - d):
                dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
        return dp[0] > 0


"""
The idea is based on minimax algorithm for adversarial game playing.
p1 tries to maximize his return by calling pmax. p2 tries to minimize p1's return by calling pmin.

pmin(i, j) => Given a pile from i...j and its p2's turn to play, return what p1 will get.
pmax(i, j) => Given a pile from i..j and its p1's turn to play, return what p1 will get.

In my logic, I am simply calculating what is the value that p1 will get if both play optimally. 
The value for p2 is the remaining and p1 > p2 tells if p1 will win.
"""
class Solution2:
    def stoneGame(self, piles):
        def pmin(i, j):
            if (i,j) in mincache: return mincache[(i,j)]
            if i == j: return 0
            mincache[(i,j)] =  min(pmax(i+1, j), pmax(i, j-1))
            return mincache[(i,j)]

        def pmax(i, j):
            if (i,j) in maxcache: return maxcache[(i,j)]
            if i == j: return piles[i]
            maxcache[(i,j)] =  max(piles[i] + pmin(i+1, j), pmin(i, j-1) + piles[j])
            return maxcache[(i,j)]

        mincache, maxcache = {}, {}
        p1 = pmax(0, len(piles)-1)
        p2 = sum(piles) - p1
        return p1 > p2

class Solution3:
    def stoneGame(self, piles):
        # If solution to piles[:n-1] and  piles[1:n] and piles[2:]
        # was known then how do we get the complete solution?
        # Possibilities:
        #   1.1 Alex picks from start and Lee from the start of the remaining piles. Then problem reduces to piles[2:]
        #   2.1: Alex picks from start and Lee from the end of the remaining piles.
        #   2.2: Alex picks from end and Lee picks from start.
        #       => Then problem reduces to piles[1:n]
        #   3. Alex picks from end and Lee picks from the end of the remaining piles. Then problem reduces to piles[:n-1]
        memo = {}

        def helper(alex, lee, start, end):
            if start > end:
                return alex > lee
            if (start, end) in memo:
                return memo[(start, end)]
            ret = (helper(alex + piles[start], lee + piles[end], start + 1, end - 1) or
                   helper(alex + piles[start], lee + piles[start + 1], start + 2, end) or
                   helper(alex + piles[end], lee + piles[start], start + 1, end - 1) or
                   helper(alex + piles[end], lee + piles[end - 1], start, end - 2))
            memo[(start, end)] = ret
            return ret

        return helper(0, 0, 0, len(piles) - 1)


"""
Approach 1: Dynamic Programming
Intuition

Let's change the game so that whenever Lee scores points, it deducts from Alex's score instead.

Let dp(i, j) be the largest score Alex can achieve where the piles remaining are piles[i], piles[i+1], ..., piles[j]. 
This is natural in games with scoring: we want to know what the value of each position of the game is.

We can formulate a recursion for dp(i, j) in terms of dp(i+1, j) and dp(i, j-1), 
and we can use dynamic programming to not repeat work in this recursion. 
(This approach can output the correct answer, because the states form a DAG (directed acyclic graph).)

Algorithm

When the piles remaining are piles[i], piles[i+1], ..., piles[j], the player who's turn it is has at most 2 moves.

The person who's turn it is can be found by comparing j-i to N modulo 2.

If the player is Alex, then she either takes piles[i] or piles[j], increasing her score by that amount. 
Afterwards, the total score is either piles[i] + dp(i+1, j), or piles[j] + dp(i, j-1); and we want the maximum possible score.

If the player is Lee, then he either takes piles[i] or piles[j], decreasing Alex's score by that amount. 
Afterwards, the total score is either -piles[i] + dp(i+1, j), or -piles[j] + dp(i, j-1); and we want the minimum possible score.

"""
class Solution4:
    def stoneGame(self, piles):
        N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j: return 0
            parity = (j - i - N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

        return dp(0, N - 1) > 0


p = [5,3,4,5]
a = SolutionLee11()
print(a.stoneGame(p))
