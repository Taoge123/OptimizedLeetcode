
"""
https://zhuanlan.zhihu.com/p/56427443
https://www.geeksforgeeks.org/burst-balloon-to-maximize-coins/

dp[left][right] = max(dp[left][right], num[left]*num[i]*num[right] + dp[left][i] + dp[i][right])


Given n balloons, indexed from 0 to n-1.
Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If the you burst balloon i
you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i.
 After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

"""
"""
Better idea

We then think can we apply the divide and conquer technique? After all there seems to be many self similar sub problems from the previous analysis.

Well, the nature way to divide the problem is burst one balloon and separate the balloons 
into 2 sub sections one on the left and one one the right.
However, in this problem the left and right become adjacent and have effects on the maxCoins in the future.

Then another interesting idea come up. Which is quite often seen in dp problem analysis. 
That is reverse thinking. Like I said the coins you get for a balloon does not depend on the balloons already burst. Therefore
instead of divide the problem by the first balloon to burst, we divide the problem by the last balloon to burst.

Why is that? Because only the first and last balloons we are sure of their adjacent balloons before hand!

For the first we have nums[i-1]*nums[i]*nums[i+1] for the last we have nums[-1]*nums[i]*nums[n].

OK. Think about n balloons if i is the last one to burst, what now?

We can see that the balloons is again separated into 2 sections. 
But this time since the balloon i is the last balloon of all to burst, 
the left and right section now has well defined boundary and do not affect each other! 
Therefore we can do either recursive method with memoization or dp.

Final

Here comes the final solutions. Note that we put 2 balloons with 1 as boundaries 
and also burst all the zero balloons in the first round since they won't give any coins.
The algorithm runs in O(n^3) which can be easily seen from the 3 loops in dp solution.
"""

class Solution1:
    def maxCoins(self, iNums):
        nums = [1] + [i for i in iNums if i > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                                          nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]


# Basic idea
# https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
# Transition function explanation
# https://leetcode.com/problems/burst-balloons/discuss/76229/For-anyone-that-is-still-confused-after-reading-all-kinds-of-explanations.../240802/
from functools import lru_cache
class Solution2:
    def maxCoins(self, nums):
        N = len(nums)
        nums.append(1) # nums[-1] == nums[N]
        @lru_cache(None)
        def recur(s=0, e=N):
            if e == s:
                return 0
            rv = 0
            for t in range(s, e):
                rv = max(rv, recur(s, t) + recur(t+1, e) + (nums[s-1]*nums[t]*nums[e]))
            return rv
        return recur()


"""
Analysis:
We need to find a way to divide the problems. If we start from the first balloon, 
we can't determine the left/right for the number in each sub-problem, If we start from the last balloon, we can.
We can see the transformation equation is very similar to the one for matrix multiplication.

dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) # i < k < j
This is a typical interval DP problem. Because the order of the number extracted matters, 
we need to do a O(n^3) DP. If we only need to expand the interval to the left or right, we only need to do a O(n^2) DP.
"""
# Top-down:
class Solution3:
    def maxCoins(self, nums):

        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1: # in memory or gap < 2
                return dp[i][j]
            coins = 0
            for k in range(i+1, j): # find the last balloon
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n-1)


# Bottom-up:
class Solution4:
    def maxCoins(self, nums):
   
        nums = [1] + nums + [1]  # build the complete array 
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n - 1]


"""
Before started, I removed all balloons with number 0, and put an additional "1" at the beginning and end, 
for that based on the definition of this problem, one can imagine there're implicitly two "1" balloons 
at the beginning and end but would never be burst. The balloon array now becomes: 
[1,...,x,x,x,x,x,x,...,1], where the x's are original nonzero balloons.

I feel the trickiest part is to sort out what you really need to calculate in each DP sub-problem. 
In each sub-problem I have 3 pointers "l", "m" and "r" located as below:

       l   m     r
  [...,x,x,x,x,x,x,...]
I focus on the region (l,r), and assign m as the last balloon to be burst in this region. I need to calculate:

max coins after the balloons in region (l,m) are burst

max coins after the balloons in region (m,r) are burst

nums[l]*nums[m]*nums[r]

Note I'm using exclusive region notation, which means the lth and rth balloons are not burst in this sub-problem.

With each iteration I gradually increase the interval between balloons l and r. 
Such process is equivalent to beginning from the 1st burst balloon. As the interval to be considered increases, 
all the possible combination of sub-intervals within current interval would have been calculated in previous iterations.

In the end I just return the regional max coins excluding the first and the last balloons, 
which are the 2 extra balloons I appended before started (now you can see why they're needed).
"""

class Solution5:
    def maxCoins(self, nums):

        nums = [1] + [n for n in nums if n != 0] + [1]
        regional_max_coins = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for balloons_to_burst in range(1, len(nums) - 1):  # number of balloons in (l,r) region
            for l in range(0, len(nums) - balloons_to_burst - 1):  # for m and r to be assigned legally
                r = l + balloons_to_burst + 1
                for m in range(l + 1, r):
                    regional_max_coins[l][r] = max(regional_max_coins[l][r],
                                                   regional_max_coins[l][m] + regional_max_coins[m][r] + nums[l] * nums[
                                                       m] * nums[r])
        return regional_max_coins[0][-1]


class Solution6:
    def maxCoins(self, nums):
        memo, nums = {}, [1] + [num for num in nums if num] + [1]
        def dfs(l, r):
            if r - l == 1: return 0
            if (l, r) not in memo: memo[(l, r)] = max(nums[l] * nums[i] * nums[r] + dfs(l, i) + dfs(i, r) for i in range(l + 1, r))
            return memo[(l, r)]
        return dfs(0, len(nums) - 1)


"""
动态规划问题的又一难点就是更新顺序问题，显然，我们为了更新更长的数组的最优解，我们需要先更新短的数组。

以长度为 6 的数组为例：

更新顺序应该为：

dp[0][2], dp[1][3], dp[2][4], dp[3][5]

dp[0][3], dp[1][4], dp[2][5]

dp[0][4], dp[1][5]

dp[0][5]
"""
class Solution7:
    def maxCoins(self, nums: 'List[int]') -> 'int':
        n = len(nums) + 2
        nums.append(1)
        nums.insert(0, 1)
        dp = [[0 for i in range(n)] for i in range(n)]
        for k in range(2, n + 2):
            for left in range(n - k):
                right = left + k;
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                                          nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][-1]


"""
This is a DP problem.

First, we define the f[i][j] (i+1<j) as the maxmium value of range we can get from range [i, j]. 
For example, if list is [2,2,2], f[1][3] 's maxmium value and only value is 8.

and the formula to calculate particular value from subset is like below. 
And, we could notice that, the range of subset is contained in side range (i, j), we could compute from smallest range to largest range.

f[i][j] = max( f[i][mid] + f[mid][j] + nums[i] * nums[mid] * nums[j] )    # i < mid < j

and with O(N^3) for loop, we could get answer
"""
class Solution8:
    def maxCoins(self, nums):

        N = len(nums)
        nums = [1] + nums + [1]

        f = [[0] * (N + 2) for _ in range(N + 2)]

        for length in range(2, N + 2):
            for i in range(N - length + 2):
                j = i + length
                mij = nums[i] * nums[j]
                for mid in range(i + 1, j):
                    v = f[i][mid] + f[mid][j] + mij * nums[mid]
                    if v > f[i][j]:
                        f[i][j] = v

        return f[0][N + 1]


"""
解题方法
这个是个DP的题目，当然也可以通过记忆化搜索的方式解决。

令dfs(i, j) 和 c[i][j]是在第[i, j]闭区间上打破气球能获得最大值。
那么，在其中找到一个不打破的气球k，则可以得到以下关系：

c[i][j] = max(c[i][j], self.dfs(nums, c, i, k - 1) + nums[i - 1] * nums[k] * nums[j + 1] + self.dfs(nums, c, k + 1, j))
1
含义是，我们找出在[i, k - 1]、[k + 1, j]闭区间打气球的分数最大值，然后会把第i - 1和第j + 1个气球保留下来，
让这两个气球和第k个气球相乘，最后求三个加法。

模拟左右两边的气球的方法是直接添加上首尾各一个1，同时使用记忆化能加速不少，也为下一步的DP提供思路。

时间复杂度是O(N^2 * log(N))(不会算…)，空间复杂度是O(N)。
"""


class Solution9:
    def maxCoins(self, nums):

        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        c = [[0] * (n + 2) for _ in range(n + 2)]
        return self.dfs(nums, c, 1, n)

    def dfs(self, nums, c, i, j):
        if i > j: return 0
        if c[i][j] > 0: return c[i][j]
        if i == j: return nums[i - 1] * nums[i] * nums[i + 1]
        res = 0
        for k in range(i, j + 1):
            res = max(res,
                      self.dfs(nums, c, i, k - 1) + nums[i - 1] * nums[k] * nums[j + 1] + self.dfs(nums, c, k + 1, j))
        c[i][j] = res
        return c[i][j]


"""
第二种解法是使用DP。

DP一般都可以通过记忆化搜索来改出来，但是我不会。。很遗憾，参考了别人的代码，还是没搞懂。。
"""
class Solution10:
    def maxCoins(self, nums):

        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for len_ in range(1, n + 1):
            for left in range(1, n - len_ + 2):
                right = left + len_ - 1
                for k in range(left, right + 1):
                    dp[left][right] = max(dp[left][right], dp[left][k - 1] + nums[left - 1] * nums[k] * nums[right + 1] + dp[k + 1][right])
        return dp[1][n]


"""
解题思路：
动态规划（Dynamic Programming）

时间复杂度O(n ^ 3)

参考peisi的答案：https://leetcode.com/discuss/72216/share-some-analysis-and-explanations

以最后被爆破的气球m为界限，把数组分为左右两个子区域

状态转移方程：

dp[l][r] = max(dp[l][r], nums[l] * nums[m] * nums[r] + dp[l][m] + dp[m][r])
dp[l][r]表示扎破(l, r)范围内所有气球获得的最大硬币数，不含边界；

l与r的跨度k从2开始逐渐增大；

三重循环依次枚举范围跨度k，左边界l，中点m；右边界r = l + k；

状态转移方程在形式上有点类似于Floyd最短路算法。"""


class SolutionTony:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * (n + 2) for i in range(n)]

        for len_ in range(2, n):
            for left in range(n - len_):
                right = left + len_
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                                          dp[left][i] + dp[i][right] + nums[left] * nums[i] * nums[right])
        return dp[0][n - 1]


a = SolutionTony()
print(a.maxCoins([3,1,5,8]))





