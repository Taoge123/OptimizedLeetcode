
"""
https://kingsfish.github.io/2017/07/23/Leetcode-474-Ones-and-Zeros/
https://leetcode.com/problems/ones-and-zeroes/discuss/177368/Python-Clear-Explanation-from-Recursion-to-DP
https://leetcode.com/problems/ones-and-zeroes/discuss/95851/4-Python-solution-with-detailed-explanation

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively.
On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings
that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
"""

"""
This question is very similar to a 0-1 knapsack, the transition function is

dp(k, x, y) = max(dp(k-1, x-z, y-o) + 1, dp(k-1, x, y))   (z is zeroes in strs[k], o is ones in strs[k])
dp(k, x, y) is the maximum strs we can include when we have x zeros, 
y ones and only the first k strs are considered.

dp(len(strs), M, N) is the answer we are looking for

I first implemented a dfs + memoization, which gets MLE, so I created a bottom up style dp.
With bottom up, we can use something called "rolling array" to optimize space complexity from O(KMN) to O(MN)
"""
"""
dp(k, x, y) = max(dp(k-1, x-z, y-o) + 1, dp(k-1, x, y))
This is the orignal state transition funciton. The implementation optimize the space complexity. 
It used only two dimensional array dp(x, y). Think like this, 
when at k iteration(the outer loop), we want to keep dp(x-z, y-o) and dp(x,y) are the state at k-1. 
Because of this dp(x, y) is depending on something in front of it dp(x-z, y-o), 
that's why we want to loop x and y from m and n, 
otherwise at k iteration, dp(x-z, y-o)is already updated, are the state at k not k-1.
"""
"""
Consider a typical 0-1 knapsack problem, dp[i][c] = max(dp[i-1][c], dp[i-1][c-w[i]] + v[i]), 
where dp[i][c] is the max value we can get considering the first i items being put into a knapsack with capacity c,
 w[i] is the weight of ith item, and v[i] is value. A naive implementation of this is to use a 2D array dp. 
 However, based on the observation that the value of dp[i][c] is always based on values one row above (dp[i-1]) 
 and to its left, we don't need to keep all previous computed results (dp[i-2] and above). 
 If we replace the 2D array, dp, with 1D array, say ra, right before starting the ith iteration, 
 ra contains values from i-1th iteration. If we iterate ra from right to left, 
 and when we are trying to compute ra[j], we can be sure that all elements to the left of ra[j], 
 including ra[j], are from previous iteration, which are the values we want use. 
 This technique is sometimes referred to as "rolling array". 
 And this problem is a 2D extension of a 1D 0-1 knapsack, and we use "rolling array" to reduce dp from 3D to 2D.
"""

"""
这道题是一道典型的应用DP来解的题，如果我们看到这种求总数，而不是列出所有情况的题，
十有八九都是用DP来解，重中之重就是在于找出递推式。
如果你第一反应没有想到用DP来做，想得是用贪心算法来做，比如先给字符串数组排个序，让长度小的字符串在前面，
然后遍历每个字符串，遇到0或者1就将对应的m和n的值减小，这种方法在有的时候是不对的，
比如对于{"11", "01", "10"}，m=2，n=2这个例子，我们将遍历完“11”的时候，把1用完了，
那么对于后面两个字符串就没法处理了，而其实正确的答案是应该组成后面两个字符串才对。
所以我们需要建立一个二维的DP数组，其中dp[i][j]表示有i个0和j个1时能组成的最多字符串的个数，
而对于当前遍历到的字符串，我们统计出其中0和1的个数为zeros和ones，
然后dp[i - zeros][j - ones]表示当前的i和j减去zeros和ones之前能拼成字符串的个数，
那么加上当前的zeros和ones就是当前dp[i][j]可以达到的个数，我们跟其原有数值对比取较大值即可，
所以递推式如下：

dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1);

有了递推式，我们就可以很容易的写出代码如下：
"""
class Solution1:
    def findMaxForm(self, strs, m, n):

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        def count(s):
            return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')

        for z, o in [count(s) for s in strs]:
            for x in range(m, -1, -1):
                for y in range(n, -1, -1):
                    if x >= z and y >= o:
                        dp[x][y] = max(1 + dp[x - z][y - o], dp[x][y])

        return dp[m][n]


class Solution2:
    class Solution:
        def findMaxForm(self, strs, m, n):

            if len(strs) == 0:
                return 0
            dp = [[0] * (n + 1) for y in range(m + 1)]
            for s in strs:
                x = s.count('0')
                y = len(s) - x
                for j in range(m, x - 1, -1):
                    for k in range(n, y - 1, -1):
                        dp[j][k] = max(dp[j][k], dp[j - x][k - y] + 1)
            return dp[m][n]

"""
We allocate a list of size length x m x n to store all possibilities of subproblems 
with m1 and n1 up to m and n. The idea is the same as the recursive solution: 
if a string can be included in a solution, we have two options: use it or skip it.
"""


class Solution3:

    def findMaxForm(self, strs, m, n):
        if not m and not n:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for string in strs:
            zeros, ones = string.count('0'), string.count('1')
            for z in range(m, zeros - 1, -1):
                for o in range(n, ones - 1, -1):
                    dp[z][o] = max(dp[z][o], dp[z - zeros][o - ones] + 1)

        return dp[m][n]

"""
题目大意
我们现在从数组中每个字符串都有一些0和1，问给了m个0，n个1，
从数组中取出最多的字符串，这些字符串中1和0的出现次数之和不超过m，n.

解题方法
看到这个题第一个感觉是贪心，但是想了想，无论是贪心少的还是贪心多的，都会影响到后面选取的变化，所以不行。

遇到这种求最多或最少的次数的，并且不用求具体的解决方案，一般都是使用DP。

这个DP很明白了，定义一个数组dp[m+1][n+1]，代表m个0, n个1能组成的最长字符串。
遍历每个字符串统计出现的0和1得到zeros和ones，所以第dp[i][j]的位置等于dp[i][j]和dp[i - zeros][j - ones] + 1。
其中dp[i - zeros][j - ones]表示如果取了当前的这个字符串，那么剩下的可以取的最多的数字。

这个题用Counter竟然不通过，使用两个常量去做统计居然就行了。

时间复杂度有点难计算，大致是O(MN * L), L 是数组长度，空间复杂度是O(MN).
"""


class Solution11:
    def findMaxForm(self, strs, m, n):

        # m个0, n个1能组成的最长字符串
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for str in strs:
            zeros, ones = 0, 0
            for c in str:
                if c == "0":
                    zeros += 1
                elif c == "1":
                    ones += 1
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]


"""
题目大意：
给定一组01字符串strs。求用m个0和n个1最多可以组成多少个strs中的字符串。

解题思路：
动态规划（Dynamic Programming）

二维01背包问题（Knapsack Problem）

状态转移方程：

for s in strs:
    zero, one = s.count('0'), s.count('1')
    for x in range(m, zero - 1, -1):
        for y in range(n, one - 1, -1):
            dp[x][y] = max(dp[x - zero][y - one] + 1, dp[x][y])

上式中，dp[x][y]表示至多使用x个0，y个1可以组成字符串的最大数目
"""
class Solution22:
    def findMaxForm(self, strs, m, n):

        dp = [[0] * (n + 1) for x in range(m + 1)]
        for s in strs:
            zero, one = s.count('0'), s.count('1')
            for x in range(m, zero - 1, -1):
                for y in range(n, one - 1, -1):
                    dp[x][y] = max(dp[x - zero][y - one] + 1, dp[x][y])
        return dp[m][n]

"""
第一种解法
这是一个多维的0-1背包问题，只是把背包容量的大小换成了0和1的个数，而宝石换成了字符串，
宝石的重量为字符串中0和1的个数，宝石价值都为1。

状态和递推式和0-1背包问题类似。因为“背包”容量是2维的，所以存储状态的数组是3维的，
状态dp[i][j][k]表示前i个字符串中能用j个0和k个1组成的最大字符串数。
这样的话状态就已经确定下来，剩下的就是寻找转移方程了。

字符串之间的转移是如何进行的呢？
其实当我们考虑dp[i][j][k]时，我们讨论的是要不要组成第i个字符串，假设第i个字符串的0和1的个数分别为zeros和ones。
如果不组成这个字符串，那么dp[i][j][k]的值就和dp[i - 1][j][k]的值是一样的；
如果组成这个字符串，那么dp[i][j][k]就应该是dp[i - 1][j - zeros][k - ones] + 1，
也即前i - 1的字符串中除去第i个字符串使用的0和1所剩下的0和1所能组成的最大字符串数量再加上1（组成了第i个字符串，所以+1）。
这样就得到了递推式：

dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - zeros][k - ones])

这个算法的时间复杂度为O(lmn)，其中l是字符串数组的长度，空间复杂度也是O(lmn)，
"""

"""
0-1背包问题中的空间优化方法
0-1背包问题有优化空间复杂度的方法。类似的，这一题也可以将三维的数组优化成二维，字符串数量那一维删去，就可以得到空间复杂度为O(mn)的算法。

以下图的0-1背包问题作为讲解。

状态数组
状态数组
我们可以看到，在每一次计算d[i][j]时，我们并没有用到所有的状态，只是前一行的两个状态。
这样的话状态存储的就能从L x m优化成2 x m，然后轮流使用这两行进行状态即可。

但是轮流使用还是很麻烦，那么有没有进一步的优化空间呢。从上面的递推式我们可以发现，
当前的状态仅仅使用上一行的两个位置的状态，那么我们完全可以使用1 x m的数组进行存储。
那么状态转移方程就变成了

d[j] = max(d[j], d[j - w] + v)

d[i - 1][j - w]			d[i - 1][j]
d[i][j]
左边的d[j]是第二行的d[i][j]，而右边是上一行的d[i - 1][j]，d[j - w]
也是上一行的d[i - 1][j - w]。但是这样有个问题，如果d[i][j + 1]在更新的时候刚好要用到d[i - 1][j]，
而这个时候d[i - 1][j]已经被更新成为了d[i][j]，那么结果就会出现错误。
如果解决这个问题呢？其实只需要将j的迭代顺序从0 -> N变成倒序即N -> 0即可。
这样的话就算d[i][j + 1]在更新的时候要用上d[i - 1][j]，d[j]也就是旧的还未更新之前的d[i - 1][j]。
这样就将0-1背包的空间复杂度从O(lm)降到了O(m)。

Ones and Zeros 问题中的空间优化方法 类似于上面的0-1背包问题，
在计算dp[i][j][k]时，我们只用到了dp[i - 1][j][k]和dp[i - 1][j - zeros][k - ones]两个状态，
因此将第二维和第三维的循环变量倒序，然后修改一下状态转移方程为

d[j][k] = max(d[j][k], d[j - zeros][k - ones] + 1)
"""







strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3

a = Solution22()
print(a.findMaxForm(strs, m, n))




