

"""
https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/156018/Python-solution-with-explanation
https://univasity.iteye.com/blog/1170216

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x.
You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

"""
"""
For each number x in range[i~j]
we do: result_when_pick_x = x + max{DP([i~x-1]), DP([x+1, j])}
--> // the max means whenever you choose a number, 
the feedback is always bad and therefore leads you to a worse branch.
then we get DP([i~j]) = min{xi, ... ,xj}
--> // this min makes sure that you are minimizing your cost.
"""
"""
More readable and easy to write bottom up solution:

why make the size to (n + 2)*(n + 2)?
the edge case we need to deal with is:
1: for M[1][?], when k = 1, then the induction rule will need M[0][n] 
which should be ignored. We solve this by marking it as 0(i.e. M[0][?] = 0 or just not set the value which makes it 0 default)
2: for M[?][n], when k = n, then the induction rule will need M[n + 1][n] 
which is indexOutOfBound and should be ignored. We solve this by expanding the 2D DP matrix size to (n + 2) * (n + 2)
How to write the two for loops?
if we draw the matrix, then according to the induction rule: 

M[i][j] = k + Math.max(M[i][k - 1], M[k + 1][j]) for k = [i : j], 

we notice that M[i][k - 1] is in the left of M[i][j], 
and M[k + 1][j] is to the bottom of M[i][j]. 
So we need to compute these value before calculating M[i][j]. 
So we write the matrix from left to right, from bottom to top and since i <= j, 
so we can just iterate half of matrix by starting j from i.
"""
"""
I feel like this is one of the classical kind of DP problem, so here I decided wrote down the thinking process for this problem for futuer record.

First we have following observation:

dp[i][j]: min money we need to guarantee a win for numbers from i ->j includisve
Following definition we can complete other typical DP components:

init: dp = [[0 for _ in  range(n+1)] for _  in range(n + 1)], dp[i][i] = 0 for i from 0->n
transition: dp[i][j] = k + max(dp[i][k-1], dp[k+1][j]), for k = i -> j inclusive
return: dp[1][n]
One thing I always felt tricky is the way to iterative over dp matrix 
becuase for this kind of problem we need to iterative over the diag. 
I personally like following template:

for start in range(1, n+1):
    for j in range(start, n+1):
		i = j - start
		update dp[i][j]
		
		. . . . 
		. . . . 
		. . . . 
		. . . .
		
"""
# So basically we iterative over column j, and compute i from j.
# With above components it is trivial to write following code:

class Solution1:
    def getMoneyAmount(self, n):

        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for start in range(1, n + 1):
            for j in range(start, n + 1):
                i = j - start
                dp[i][j] = min(i + dp[i + 1][j], j + dp[i][j - 1])
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k - 1], dp[k + 1][j]))
        return dp[1][n]

"""
l represents the length of the current range. i represents the starting index of the current range.
Building up the DP table until l is n.
"""
class Solution2:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for i in range(n + 1)]
        for l in range(2, n + 1):
            for i in range(1, n + 2 - l):
                dp[l][i] = min(j + max(dp[j - i][i], dp[i + l - j - 1][j + 1]) for j in range(i, i + l - 1))
        return dp[-1][1]


"""
此题是之前那道Guess Number Higher or Lower的拓展，难度增加了不少，根据题目中的提示，
这道题需要用到Minimax极小化极大算法，关于这个算法可以参见这篇讲解，并且题目中还说明了要用DP来做，
那么我们需要建立一个二维的dp数组，其中dp[i][j]表示从数字i到j之间猜中任意一个数字最少需要花费的钱数，
那么我们需要遍历每一段区间[j, i]，维护一个全局最小值global_min变量，
然后遍历该区间中的每一个数字，计算局部最大值local_max = k + max(dp[j][k - 1], dp[k + 1][i])，
这个正好是将该区间在每一个位置都分为两段，然后取当前位置的花费加上左右两段中较大的花费之和为局部最大值，
为啥要取两者之间的较大值呢，因为我们要cover所有的情况，就得取最坏的情况。
然后更新全局最小值，最后在更新dp[j][i]的时候看j和i是否是相邻的，相邻的话赋为i，
否则赋为global_min。这里为啥又要取较小值呢，因为dp数组是求的[j, i]范围中的最低cost，
比如只有两个数字1和2，那么肯定是猜1的cost低，是不有点晕，没关系，博主继续来绕你。
我们想，如果只有一个数字，那么我们不用猜，cost为0。如果有两个数字，比如1和2，我们猜1，
即使不对，我们cost也比猜2要低。如果有三个数字1，2，3，那么我们就先猜2，根据对方的反馈，
就可以确定正确的数字，所以我们的cost最低为2。如果有四个数字1，2，3，4，那么情况就有点复杂了，
那么我们的策略是用k来遍历所有的数字，然后再根据k分成的左右两个区间，取其中的较大cost加上k。

当k为1时，左区间为空，所以cost为0，而右区间2，3，4，根据之前的分析应该取3，所以整个cost就是1+3=4。

当k为2时，左区间为1，cost为0，右区间为3，4，cost为3，整个cost就是2+3=5。

当k为3时，左区间为1，2，cost为1，右区间为4，cost为0，整个cost就是3+1=4。

当k为4时，左区间1，2，3，cost为2，右区间为空，cost为0，整个cost就是4+2=6。

综上k的所有情况，此时我们应该取整体cost最小的，即4，为最后的答案，这就是极小化极大算法，参见代码如下：
"""
"""
题目大意
这个题应该理解为玩家是个绝对聪明的个体，他每一步都能使用最优的策略去查找要求的这个数字。那么，问找出1～n这里面的某个数字最少需要的花费。

解题方法
这个题说实话，我还真是不会，以下是细语呢喃的讲解，非常详细。建议大家看原博。
"""
"""
这题要求我们在猜测数字y未知的情况下（1~n任意一个数），要我们在最坏情况下我们支付最少的钱。也就是说要考虑所有y的情况。

我们假定选择了一个错误的数x，（1<=x<=n && x!=y ）那么就知道接下来应该从[1,x-1 ] 或者[x+1,n]中进行查找。
假如我们已经解决了[1,x-1] 和 [x+1,n]计算问题，我们将其表示为solve(L,x-1)
和solve(x+1,n)，那么我们应该选择max(solve(L,x-1),solve(x+1,n))
这样就是求最坏情况下的损失。总的损失就是 f(x) = x + max(solve(L,x-1),solve(x+1,n))

那么将x从1~n进行遍历，取使得 f(x) 达到最小，来确定最坏情况下最小的损失，也就是我们初始应该选择哪个数。

上面的说法其实是一个自顶向下的过程（Top-down），可以用递归来解决。很容易得到如下的代码（这里用了记忆化搜索）：
"""

class SolutionTopDown:
    def getMoneyAmount(self, n):
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        return self.solve(dp, 1, n)

    def solve(self, dp, L, R):
        if L >= R:
            return 0
        if dp[L][R]:
            return dp[L][R]
        dp[L][R] = min(i + max(self.solve(dp, L, i - 1), self.solve(dp, i + 1, R)) for i in range(L, R + 1))
        return dp[L][R]

# 把递归改为迭代，方法如下：
class SolutionBottomUp:
    def getMoneyAmount(self, n):

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for l in range(n - 1, 0, -1):
            for r in range(l + 1, n + 1):
                dp[l][r] = min(i + max(dp[l][i - 1], dp[i + 1][r]) for i in range(l, r))
        return dp[1][n]

"""
解题思路：
动态规划（Dynamic Programming）

参考：https://discuss.leetcode.com/topic/51356/two-python-solutions

状态转移方程：

dp[i][j] = min(k + max(dp[i][k - 1], dp[k + 1][j]))
"""
class Solution3:
    def getMoneyAmount(self, n):

        dp = [[0] * (n+1) for _ in range(n+1)]
        for gap in range(1, n):
            for lo in range(1, n+1-gap):
                hi = lo + gap
                dp[lo][hi] = min(x + max(dp[lo][x-1], dp[x+1][hi]) for x in range(lo, hi))
        return dp[1][n]

"""
记忆化搜索：

自顶向下（Top-down Approach）求解，采用辅助数组dp记录已经计算过的结果，减少重复计算。
"""
class Solution4:
    def getMoneyAmount(self, n):

        dp = [[0] * (n+1) for _ in range(n+1)]
        def solve(lo, hi):
            if lo < hi and dp[lo][hi] == 0:
                dp[lo][hi] = min(x + max(solve(lo,x-1), solve(x+1,hi)) for x in range(lo, hi))
            return dp[lo][hi]
        return solve(1, n)




"""
-----------------------------------------------------------------------------
题目大意：
我们来玩猜数字游戏。游戏规则如下：

我挑选一个1到n之间的数字。你来猜我选的是哪个数字。

每一次你猜错，我都会告诉你数字高了还是低了。

你可以调用一个预定义的API guess(int num)，返回3种结果 (-1, 1, 或 0)：

-1 : 我的数字更低
 1 : 我的数字更高
 0 : 恭喜你！猜对了！
测试用例如题目描述。

解题思路：
二分查找（Binary Search）"""


class Solution11:
    def guessNumber(self, n):

        left, right = 1, n
        while left <= right:
            mid = (left + right) >> 1
            trial = guess(mid)
            if trial == -1:
                right = mid - 1
            elif trial == 1:
                left = mid + 1
            else:
                return mid


a = Solution1()
print(a.getMoneyAmount(10))


