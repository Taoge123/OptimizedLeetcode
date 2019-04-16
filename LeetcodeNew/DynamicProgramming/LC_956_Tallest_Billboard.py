
"""
https://blog.csdn.net/xx_123_1_rj/article/details/86557102
https://blog.csdn.net/qq_17550379/article/details/85070792



You are installing a billboard and want it to have the largest height.  The billboard will have two steel supports, one on each side.  Each steel support must be an equal height.

You have a collection of rods which can be welded together.  For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation.  If you cannot support the billboard, return 0.



Example 1:

Input: [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
Example 2:

Input: [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
Example 3:

Input: [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.


Note:

0 <= rods.length <= 20
1 <= rods[i] <= 1000
The sum of rods is at most 5000.

956. 最高的广告牌
问题描述：
你正在安装一个广告牌，并希望它高度最大。这块广告牌将有两个钢制支架，两边各一个。每个钢支架的高度必须相等。

你有一堆可以焊接在一起的钢筋 rods。举个例子，如果钢筋的长度为1、2和 3，则可以将它们焊接在一起形成长度为6 的支架。

返回广告牌的最大可能安装高度。如果没法安装广告牌，请返回 0。

示例 1：

输入：[1,2,3,6]
输出：6
解释：我们有两个不相交的子集 {1,2,3} 和 {6}，它们具有相同的和 sum = 6。

示例 2：

输入：[1,2,3,4,5,6]
输出：10
解释：我们有两个不相交的子集 {2,3,5} 和 {4,6}，它们具有相同的和 sum = 10。

提示：

0 <= rods.length <= 20
1 <= rods[i] <= 1000
钢筋的长度总和最多为 5000


"""
"""
Explanation:
dp[d] mean the maximum pair of sum we can get with pair difference d
For example, if have a pair of sum (a, b) with a > b, then dp[a - b] = b
If we have dp[diff] = a, it means we have a pair of sum (a, a + diff).
And this is the biggest pair with difference = a

dp is initializes with dp[0] = 0;

Assume we have an init state like this
------- y ------|----- d -----|
------- y ------|

case 1
If put x to tall side
------- y ------|----- d -----|----- x -----|
------- y ------|

We update dp[d + x] = max(dp[d + x], y )

case 2.1
Put x to low side and d >= x:
-------y------|----- d -----|
-------y------|--- x ---|

We update dp[d-x] = max( dp[d - x], y + x)

case 2.2
Put x to low side and d < x:
------- y ------|----- d -----|
------- y ------|------- x -------|
We update dp[x - d] = max(dp[x - d], y + d)

case 2.1 and case2.2 can merge into dp[abs(x - d)] = max(dp[abs(x - d)], y + min(d, x))


Time Complexity:
O(NM), where we have
N = rod.length <= 20
S = sum(rods) <= 5000
M = all possible sum = min(3^N, S)

There are 3 ways to arrange a number: in the first group, in the second, not used.
The number of difference will be less than 3^N.
The only case to reach 3^N is when rod = [1,3,9,27,81...]
"""

class SolutionLee:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for x in rods:
            for d, y in dp.items():
                dp[d + x] = max(dp.get(x + d, 0), y)
                dp[abs(d - x)] = max(dp.get(abs(d - x), 0), y + min(d, x))
        return dp[0]


"""
One Optimisation
We do the same thing for both half of rods.
Then we try to find the same difference in both results.

Time Complexity:
O(NM), where we have
N = rod.length <= 20
S = sum(rods) <= 5000
M = all possible sum = min(3^N/2, S)
"""

class SolutionLee2:
    def tallestBillboard(self, rods):
        def helper(A):
            dp = {0: 0}
            for x in A:
                for d, y in dp.items():
                    dp[d + x] = max(dp.get(x + d, 0), y)
                    dp[abs(d - x)] = max(dp.get(abs(d - x), 0), y + min(d, x))
            return dp

        dp, dp2 = helper(rods[:len(rods) / 2]), helper(rods[len(rods) / 2:])
        return max(dp[d] + dp2[d] + d for d in dp if d in dp2)


class SolutionLeeBest:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for x in rods:
            for d, y in dp.items():
                # init state
                # ------|----- d -----|      # tall side
                # - y --|                    # low  side

                # put x to tall side
                # ------|----- d -----|---- x --|
                # - y --|
                dp[d + x] = max(dp.get(d + x, 0), y)

                # put x to low side
                if d >= x:
                    # ------|----- d -----|
                    # - y --|---- x ---|
                    dp[d - x] = max(dp.get(d - x, 0), y + x)
                else:
                    # ------|----- d -----|
                    # - y --|-------- x --------|
                    dp[x - d] = max(dp.get(x - d, 0), y + d)
        return dp[0]


"""
问题分析：
（1）方法一：
把题目的的意思简化一下，其实就是这一组数据分成3组，其中两组的和一样（最大的哦），
另外一组无所谓了。不妨给每一个数字打标签分别乘，1、0、-1，总和加起来为0，且，正整数和达到最大（
每到一个值，就有三种情况考虑，如下图）

在实现方面，就可以考虑，深度优先，或者是广度优先+动规来实现。这种方法实现比较简单，但是计算量较大，开辟的空间也大，最坏的情况下为 3n 3^n3 
n
  。比较好的是，这个方法仍然可以提交AC的。具体方法有点类似背包问题：

（1）现在设置一个dp，可以python字典表示，k表示，整个序列乘上标签，之后的和，value表示这些序列中正数的和。从上图可以看出来初始化为{0:0}。

（2）接下来，就是每处理一个数，就处理一层。简单的理解就是，在上层产生的结果中，如果继续向下分析，在前面的基础上，每个结果有三种可能。

（3）处理的方法为：

cur = collections.defaultdict(int)
for s in dp:
    cur[s + i] = max(dp[s] + i, cur[s + i])  # 标记为 1 的情况，并取最大值
    cur[s] = max(dp[s], cur[s])  # 标记为 0 的情况，并取最大值
    cur[s - i] = max(dp[s], cur[s - i])  # 标记为 -1 的情况，并取最大值
dp = cur  # 更新dp

cur表示当前正在处理的层。dp表示上一层。从这个过程可以看出，其实也是一个动规过程，
依赖前面的结果，构成子问题。虽然类似于穷举法，但是在计算过程相同的可能只保留了一个。
最后，直接返回dp[0]即可。参考链接在文章下面。


"""

"""
It is like a knapsack problem.
Consider this problem as:
Given a list of numbers, multiply each number with 1 or 0 or -1, make the sum of all numbers to 0. Find a combination which has the largest sum of all positive numbers.

We can consider the sum as the key and positive number sum as the value.
We initally have dp[0] = 0

We iterate through the numbers and calculate the pairs that we got. In the case that we have same sum but different postive number sum, we only keep the largest postive number sum.

Let's run through a example, [1,2,3]
First we have {0:0}.
After 1, we have {0: 0, 1: 1, -1: 0}
After 2, we have {0:0, 2:2, -2:0, 1:1, 3:3,-1:1, -1:0,1:2,-3:0}
we will drop 1:1 and -1:0 since they have smaller value with the same key[1]and [-1]. That left us with {0:0, 2:2, -2:0, 3:3,-1:1,1:2,-3:0}
Number 3 is doing pretty much the same.
Then we will get the final result with dp[0]

"""
class Solution11:
    def tallestBillboard(self, rods):
        dp = dict()
        dp[0] = 0

        for i in rods:
            cur = collections.defaultdict(int)
            for s in dp:
                cur[s + i] = max(dp[s] + i, cur[s + i])
                cur[s] = max(dp[s], cur[s])
                cur[s - i] = max(dp[s], cur[s - i])
            dp = cur
        return dp[0]


"""
Similar to Target Sum, the difference is that in this question, 
we can treat any number num as num, -num, or0, and the final target is 0.

we can maintain a possible prefix sum map, where the key is all possible prefix sum, 
and the value is the maximum sum of positive numbers.
"""

class Solution111:
    def tallestBillboard(self, rods):
        presum = {0:0}

        for rod in rods:
            newsum = {}
            for val, pos_val in presum.items():
                newsum[val + rod] = max(newsum.get(val + rod, 0), pos_val + rod)
                newsum[val - rod] = max(newsum.get(val - rod, 0), pos_val)
                newsum[val] = max(newsum.get(val, 0), pos_val)
            presum = newsum
        return presum[0]

"""
At the very beginning, I came up with the state description:
DP[i][j] = True or False
It means if I can make two steel supports of lengths i and j.
The state description uses a 2D array. 
And you have another loop to use each rod to update the states. 
The time complexity is O(nmm).

But don't forget, we don't care every state. We only care about the best state.
For example, if we have dp[i][j] = True and dp[i+k][j+k] = True. Do we still care dp[i][j] ? No!

So the state description can be simplized to dp[dx] = len, which means we can realize the state (len, len+dx).

Details can be easily understood in my code.
The time complexity is O(nm).
"""
class Solution1111:
    def tallestBillboard(self, rods):
        dp = [-1] * (sum(rods) + 2)
        m = len(dp)
        # dp[dx] = i -> (i, i+dx)
        dp[0] = 0
        n = len(rods)
        for i in range(n):
            tmp = [0] * m
            for j in range(m):
                tmp[j] = dp[j]
            for dx in range(m):
                if tmp[dx] != -1:
                    maxlen = max(tmp[dx] + rods[i], tmp[dx] + dx)
                    minlen = min(tmp[dx] + rods[i], tmp[dx] + dx)
                    dp[maxlen - minlen] = max(minlen, dp[maxlen - minlen])
                    maxlen = max(tmp[dx], tmp[dx] + dx + rods[i])
                    minlen = min(tmp[dx], tmp[dx] + dx + rods[i])
                    dp[maxlen - minlen] = max(minlen, dp[maxlen - minlen])

        return dp[0]


"""
Maintain a dictionary mapping the difference in side heights to the greatest total length used with that difference.
Use only non-negative differences.

For each rod, update each height difference by both adding and subtracting the rod.
The solution is the greatest total length with a difference of zero.
"""

from collections import defaultdict

class Solutin11111:
    def tallestBillboard(self, rods):
        diffs = {0: 0}

        for rod in rods:

            new_diffs = defaultdict(int, diffs)
            for diff, used_len in diffs.items():
                new_diffs[diff + rod] = max(used_len + rod, new_diffs[diff + rod])
                new_diffs[abs(diff - rod)] = max(used_len + rod, new_diffs[abs(diff - rod)])

            diffs = new_diffs

        return diffs[0] // 2


import collections
class Solution1:

    def tallestBillboard(self, rods):
        dp = dict()
        dp[0] = 0  # 初始化dp

        for i in rods:
            cur = collections.defaultdict(int)
            for s in dp:  # 分三种情况考虑
                cur[s + i] = max(dp[s] + i, cur[s + i])
                cur[s] = max(dp[s], cur[s])
                cur[s - i] = max(dp[s], cur[s - i])
            dp = cur
        return dp[0]  # 返回结果


"""
（2）方法二：
现在看一下官方的解答，官方的方法是使用递归实现的，其思想采用了深度优先 加动规 的方法。

（1）令 dp[i][s] 表示使用rods[0：j] (j >= i)时最优解，而s表示，在当前路径中结合3种标签（1，0，-1）的和。

（2）很显然，把每个路径走到头，如果s=0，说明这个路径是可行的，如果不为0，说明此路径是不可行的。

（3）当然，走到头，会有很多种可能，所以选择一个最大的作为结果，即可。

（4）所以，递推公式可以表示为：dp[i][s] = max(dp[i+1][s], dp[i+1][s-rods[i]], rods[i] + dp[i+1][s+rods[i]])。

（5）这种思想采用了深度优先 ，感觉也是穷举法。
"""
from functools import lru_cache
class Solution2:
    def tallestBillboard(self, rods):
        @lru_cache(None)
        def dp(i, s):
            if i == len(rods):
                return 0 if s == 0 else float('-inf')
            # 三情况取最大
            return max(dp(i + 1, s), dp(i + 1, s - rods[i]), dp(i + 1, s + rods[i]) + rods[i])

        return dp(0, 0)


"""
解题思路

对于这个问题首先想到的解决思路是通过DFS。我们遍历rods中的元素，我们对每个元素都有如下三种考量。

放左边
放右边
不放
当我们左边钢筋的长度left和右边钢筋的长度right是一样的时候，我们就需要记录这种情况下的最大值res。
我们在初始的时候需要记录一个最大容量maxsum（sum(rods)），我们每次遍历的过程中需要更新它，
也就是我们每使用一个钢筋i，我们就要将maxsum减去相应的值rods[i]。我们接着思路递归到底的情况。

遍历完rods的最后一个元素
abs(left−right)>maxsum abs(left-right) &gt; maxsumabs(left−right)>maxsum
left+right+maxsum&lt;=res∗2 left+right+maxsum&lt;=res*2left+right+maxsum<=res∗2
第一种情况自然不用多说。第二种情况，我们最后无法得到left==right的情形，所以也要返回。
对于第三种情况，我们此时res就是最大长度了，所以直接返回就可以了。

我们在一开始的时候，也就是放入第一根钢筋的时候，我们只要考虑放和不放，而不需要考虑放左还是放右。
一切安排妥当，我们开始写代码
"""


class Solution3:
    def tallestBillboard(self, rods):

        if len(rods) == 0 or len(rods) == 1:
            return 0

        self.res = 0

        rods.sort(reverse=True)  # add sort
        remain = sum(rods)
        self.dfs(rods, remain - rods[0], 0, rods[0], 0)
        self.dfs(rods, remain - rods[0], 0, 0, 0)

        return self.res

    def dfs(self, rods, remain, i, left, right):
        if abs(left - right) > remain or \
                (left + right + remain <= self.res * 2):
            return

        if left == right and self.res < left:
            self.res = left

        i += 1
        if i == len(rods):
            return

        remain -= rods[i]
        self.dfs(rods, remain, i, left + rods[i], right)
        self.dfs(rods, remain, i, left, right + rods[i])
        self.dfs(rods, remain, i, left, right)


"""
但是我们这样做了之后超时了。我们需要一步优化，我们可以在开始的时候对rods按照从大到小排序（贪心策略）。

这个问题有个巧妙的方法，我们首先定义函数f(a,b) f(a,b)f(a,b)返回距离差是abs(a−b) abs(a-b)abs(a−b)的最大公共长度。例如


我们此时知道两者长度相差d dd，那么此时f(d)=len(red) f(d)=len(red)f(d)=len(red)。此时如果我们新加入一个钢筋x，那么我们有两种策略，第一种是加在上面
那么我们知道此时的f(d+x)=max(f(d+x),len(red)) f(d+x)=max(f(d+x), len(red))f(d+x)=max(f(d+x),len(red))。我们也可以将它加入到下面
那么我们知道此时的f(d−x)=max(f(d−x),len(red)+x) f(d-x)=max(f(d-x),len(red)+x)f(d−x)=max(f(d−x),len(red)+x)，或者也可以是下面这种
那么我们知道此时的f(x−d)=max(f(x−d),len(red)+d) f(x-d)=max(f(x-d),len(red)+d)f(x−d)=max(f(x−d),len(red)+d)。

但是这样做有什么用呢？我们虽然能保证最大的公有长度，但是这个公有长度不一定可以通过所给的rods中的元素拼凑出来啊？是的，确实是这样。
但是我们可以保证的是f(0) f(0)f(0)一定可以通过rods中的元素拼凑出来，而f(0) f(0)f(0)恰好就是我们所需要的结果，非常好的思路。
"""


class Solution33:
    def tallestBillboard(self, rods):

        mem = {0: 0}

        for i in rods:
            cur = mem.copy()
            for d, val in cur.items():
                mem[d + i] = max(mem.get(i + d, 0), val)
                mem[abs(d - i)] = max(mem.get(abs(d - i), 0), val + min(i, d))

        return mem[0]


"""
分析
题目如果用暴力求解的话会超时，暴力求解也就是每个数字有三种状态，不被选中/被选中在左边集合/被选中在右边集合，然后找左右集合相加和最大的那种情况。时间复杂度3的n次方。

题目提示是动态规划题，那么最重要的就是定义状态，差点儿把我愁坏了，然后看了解题报告。

题目求广告牌的最大可能安装高度，那定义 dp[i][j] 来表示 前 i 个支架高度差为 j 的时候，最长的公共长度。

每多添加一个支架，则这个支架其实有三个状态，1.这个支架不添加到任何一端；2.支架添加到高的一端；3.支架添加到短的一端。

1. 支架不添加到任何一端 :
   这种情况下的 dp[i][j] = dp[i-1][j] 因为第 i 个不用，所以它的最优的公共长度应该 = max( dp[i-1][j], dp[i][j] )
2. 支架添加到高的一端
   这种情况下即，高的更高， dp[i][j+h] = max(dp[i][j+h] , dp[i][j] + h)
3.支架添加到短的一端
  这种情况则是把新加进来的支架加到短的一端，也就是加长了短一端的长度，这个时候还会有两种情况，要么是短的加了一截还是短，另一种是短的加了一截变长了。把这两种情况合并一下：即
  dp[i][|j-h|] = max( dp[i][|j-h|] , dp[i-1][j] + min(j, h) )
"""

"""
思路：暴力BFS TLE；改用dp，dp[i][j]=True，表示（I,J）2部分可以分别得到i，j，
具体求解过程就是对于没来一个数，就更新一遍dp[i][j]数组，但是复杂度太大了。

仔细想想，每来rods数组中一个数，是用来改变（I,J）之间差值，所以其实只需要一维数组就够了，
dp[i]表示（I,J）差值为i时，（I,J）中 小的/大的 那个数最大是多少

But don't forget, we don't care every state. We only care about the best state.
For example, if we have dp[i][j] = True and dp[i+k][j+k] = True. 
Do we still care dp[i][j] ? No!

So the state description can be simplized to dp[dx] = len, 
which means we can realize the state (len, len+dx).

"""


class Solution4:
    def tallestBillboard(self, rods):

        if not rods: return 0
        su = sum(rods)
        dp = [-1] * (su + 1)
        dp[0] = 0
        dp2 = list(dp)

        for i in rods:
            for j in range(su + 1):
                if dp[j] == -1: continue

                # add to larger
                if j + i <= su:
                    dp2[j + i] = max(dp2[j + i], dp[j])

                # add to smaller
                if j >= i:
                    dp2[j - i] = max(dp2[j - i], dp[j] + i)
                else:
                    dp2[i - j] = max(dp2[i - j], dp[j] + j)

            dp = list(dp2)

        return dp[0]

"""
思路

动态规划。自己实在是想不出来，思路参考了酒井算协比赛部题解

记两个子列中子列和大者为big, 小者为small.

用dp[i][j]表示考虑到前i个rods的情况下，big比small子列和大j时big的最大子列和。

状态转移条件有4种：

1. 第i个rod没有使用；

2. 第i个rod给了big；

3. 第i个rod给了small，且给了small之后没有使得big和small地位反转；

4. 第i个rod给了small，且给了small之后使得big和small地位反转。

答案就是dp[n][0].

有两个注意点：

1. dp[i][0] (i>0)是可能的，因此要赋值为一个绝对值很大的负数而不能赋值为0；

2. dp[0][0] = 0.
"""
from functools import lru_cache
class Solution5:
    def tallestBillboard(self, rods):
        @lru_cache(None)
        def dp(i, s):
            if i == len(rods):
                return 0 if s == 0 else float('-inf')
            return max(dp(i + 1, s),
                       dp(i + 1, s - rods[i]),
                       dp(i + 1, s + rods[i]) + rods[i])

        return dp(0, 0)


"""
分析
在比赛的时候我能想到的最好的解法是这样的：

枚举第一组都有哪些棍子（2^20）
对于剩下的棍子，用动态规划的方法判断能否组成第一组已有的长度（5000*20）
显然这个算法是会超时的。但是也许它已经接近正解了。

解法1：-1,0,1背包
把这个问题看成是扩展版的01背包问题：对于每根棍子，我们可以把它加入背包中，不加入背包中，还可以把它从背包中减去。

令f[i][j]表示用前i根棍子能否组成和为j的长度（j有可能是负的）。
则f[i+1][j] = f[i][j] || f[i][j-rods[i+1]] || f[i][j+rods[i+1]]。
为了找到可能的最大长度，用辅助数组g[i][j]记录f[i][j]为真时，最大可能的正长度之和。算法的复杂度为O(10000*N)。[1]

解法2：中间相遇法
把rods数组分成大致相等的两半，然后对每一半都枚举每根棍子是+，-还是0。
然后对于左边的一半得到的和，在右边寻找这个和的负值是否存在。最后取最大值。算法复杂度为O(3^(N/2))。

这个算法也需要记录最大可能的正长度之和。


"""
