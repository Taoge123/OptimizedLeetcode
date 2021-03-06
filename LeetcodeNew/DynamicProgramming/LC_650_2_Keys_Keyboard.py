
"""
https://blog.csdn.net/MebiuW/article/details/76651618

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.


Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted.
Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
"""

"""
Approach #1: Prime Factorization [Accepted]
Intuition

We can break our moves into groups of (copy, paste, ..., paste). 
Let C denote copying and P denote pasting. 
Then for example, in the sequence of moves CPPCPPPPCP, the groups would be [CPP][CPPPP][CP].

Say these groups have lengths g_1, g_2, .... After parsing the first group, 
there are g_1 'A's. After parsing the second group, there are g_1 * g_2 'A's, and so on. 
At the end, there are g_1 * g_2 * ... * g_n 'A's.

We want exactly N = g_1 * g_2 * ... * g_n. If any of the g_i are composite, say g_i = p * q, 
then we can split this group into two groups (the first of which has one copy followed by p-1 pastes, 
while the second group having one copy and q-1 pastes).

Such a split never uses more moves: we use p+q moves when splitting, and pq moves previously. 
As p+q <= pq is equivalent to 1 <= (p-1)(q-1), which is true as long as p >= 2 and q >= 2.

Algorithm By the above argument, we can suppose g_1, g_2, ... is the prime factorization of N, 
and the answer is therefore the sum of these prime factors.
"""


class SolutionLee:
    def minSteps(self, n):
        if n == 1:
            return 0
        for i in range(2, n + 1):
            if n % i == 0:
                return self.minSteps(n / i) + i


"""
As a default, any number of A's can be generated by copying one A and pasting it n times, 
with the exception of 0 and 1. However, composite numbers can utilize their prime factors, 
minimizing the number of copy and paste operations. 
You can start to visualize a pattern by seeing some primitive examples:

2 - c 'A', p 'AA'
3 - c 'A', p 'AA', p 'AAA'
4 - c 'A', p 'AA', c 'AA', p 'AAAA'
5 - c 'A', p 'AA', p 'AAA', p 'AAAA', p 'AAAAA'
6 - c 'A', p 'AA', p 'AAA', c 'AAA', p 'AAAAAA'
...

Therefore, the pattern is:

1. For some prime number n, it will require n operations because it cannot be broken down into even copy and paste operations
2. For some composite number n, copy its highest factor m and paste it n / m times
"""
class Solution1:
    def minSteps(self, n):

        if n <= 1:
            return 0

        M = [i for i in range(n + 1)]

        for i in range(2, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    M[i] = min(M[i], M[j] + i // j)

        return M[-1]


class Solution2:
    def minSteps(self, n):

        # dp[x] = minimum number of steps to get x A on screen

        # maximum number of steps to get x A , is to get copy 1 A and paste it x-1 times - total x operations
        # so dp[x] = x to begin with
        dp = [i for i in range(n + 1)]
        # exception is 0 and 1, for which dp[0]=0 and dp[1]=0
        dp[0] = dp[1] = 0

        # how to divide the number x?
        # x can be expressed as a*b
        # lets say b is always higher than a
        # so highest value of b can be x                : x is prime (x can not be divided)
        # or highest value of b can be some factor of x : x is not prime
        #
        # if x is not prime, collect b As in clipboard and paste it a -1 (or x//b - 1) times -
        # collecting b As in clipboard = dp[b] + 1 (get b As:dp[b] and then "copy":1 )
        # paste b As in (a-1) times    = a - 1 = x//b - 1
        #
        # so dp[x] = dp[b] + 1 + x//b - 1 ---- where b is largest factor of x
        for i in range(2, n + 1):
            for j in range(i - 1, 1, -1):
                if (i % j == 0):
                    dp[i] = dp[j] + 1 + i // j - 1
                    break
        return dp[n]


"""

gabbu's avatar
gabbu
650
Last Edit: October 22, 2018 9:16 PM

165 VIEWS

2 Keys Keyboard https://leetcode.com/problems/2-keys-keyboard/description/

Memoization with O(N^2) time and space

x: number of 'A' in the buffer
y: number of 'A' in the textpad
At each step, we can either paste or copy+paste.
paste, cpaste = float('inf'), float('inf')
paste = MS(x, x+y, n)+1 iff x+y <= n and x > 0 i.e. we must have something to paste and by pasting the buffer we should not exceed n.
cpaste = MS(y, 2y, n)+2 iff 2y <= n
MS(x,y,n) = min(paste, cpaste)

"""

"""
这道题只给了我们两个按键，如果只能选择两个按键，那么博主一定会要复制和粘贴，此二键在手，天下我有！！！
果然，这道题就是给了我们复制和粘贴这两个按键，然后给了我们了一个A，我们的目标时利用这两个键来打印出n个A，
注意复制的时候时全部复制，不能选择部分来复制，然后复制和粘贴都算操作步骤，问我们打印出n个A需要多少步操作。
对于这种有明显的递推特征的题，我们要有隐约的感觉，一定要尝试递归和DP。递归解法一般接近于暴力搜索，
但是有时候是可以优化的，从而能够通过OJ。而一旦递归不行的话，那么一般来说DP这个大杀器都能解的。还有一点，
对于这种题，找规律最重要，DP要找出递推公式，而如果无法发现内在的联系，那么递推公式就比较难写出来了。
所以，我们需要从简单的例子开始分析，试图找规律：

当n = 1时，已经有一个A了，我们不需要其他操作，返回0

当n = 2时，我们需要复制一次，粘贴一次，返回2

当n = 3时，我们需要复制一次，粘贴两次，返回3

当n = 4时，这就有两种做法，一种是我们需要复制一次，粘贴三次，共4步，另一种是先复制一次，粘贴一次，得到AA，然后再复制一次，粘贴一次，得到AAAA，两种方法都是返回4

当n = 5时，我们需要复制一次，粘贴四次，返回5

当n = 6时，我们需要复制一次，粘贴两次，得到AAA，再复制一次，粘贴一次，得到AAAAAA，共5步，返回5

通过分析上面这6个简单的例子，我想我们已经可以总结出一些规律了，首先对于任意一个n(除了1以外)，我们最差的情况就是用n步，不会再多于n步，
但是有可能是会小于n步的，比如n=6时，就只用了5步，仔细分析一下，发现时先拼成了AAA，再复制粘贴成了AAAAAA。
那么什么情况下可以利用这种方法来减少步骤呢，分析发现，小模块的长度必须要能整除n，这样才能拆分。对于n=6，我们其实还可先拼出AA，
然后再复制一次，粘贴两次，得到的还是5。分析到这里，我想解题的思路应该比较清晰了，我们要找出n的所有因子，然后这个因子可以当作模块的个数，
我们再算出模块的长度n/i，调用递归，加上模块的个数i来更新结果res即可，参见代码如下：

 """
"""
解题方法
这道题可以转化成，给一个数字N，初始K=1，C=0然后只允许你有两种操作：

1、K = K + C （paste） 
2 、C = K （copy all）

问，如何操作可以使得最快的得到N

N>1时，其实这道题就是将N分解为M个数字的乘积，且M个数字的和最小。

比如：

2 = 1 * 1 = 2 
3 = 1 * 1 * 1 = 3 
4 = 2 * 2 = 1 * 1 * 1 * 1 = 4 
1
2
3
即求最快的把一个数分解为N个质数的和。

大神的解法，从小到大的去试探，尽量用小的数字去除就可以。
"""

class Solution3:
    def minSteps(self, n):
        res = 0
        for i in range(2, n + 1):
            while n % i == 0:
                res += i
                n /= i
        return res


"""
解题思路：
动态规划（Dynamic Programming）

dp[n]表示生成n个字符所需的最小操作次数

dp[0, .. , n]初始为∞

dp[0] = dp[1] = 0
状态转移方程：

dp[x] = min(dp[x], dp[y] + x / y) ，y ∈[1, x) 并且 x % y == 0
"""

"""
思路： 
这道题是动态规划题，状态转移方程不是很明显，需要仔细分析。 
先把dp的最小不走都设置为无穷大（0x7FFFFFFF）, 初始化条件为： dp[0]=dp[1]=0 ，状态转移方程为： 
dp[i]=min(dp[i],dp[j]+i/j),i>1,j<i且i是j的整数倍 
上述状态转移方程表示：
如果i是j的倍数，那么i可以通过粘贴(i/j-1)次j 得到, 再加上一次复制操作，那么可以通过dp[j]+i/j 次操作得到dp[i] .

"""
"""
The n will be in the range [1, 1000].
这道题是典型的递归题啊。

我的思路是，要得到 n 个 A，必然要先得到 n 的整数除数个A ，然后再粘贴而来。比如说要得到 18个A 的最小步数。 
可以是：先得到 9个A 的最小步数，再复制 粘贴1次。
也可以是：先得到 6个A 的最小步数，再复制 粘贴2次。
也可以是：先得到 3个A 的最小步数，再复制 粘贴5次。等等等等
"""

class Solution4:
    def minSteps(self, n):

        dp = [0x7FFFFFFF] * (n + 1)
        dp[0] = dp[1] = 0
        for x in range(2, n + 1):
            for y in range(1, x):
                if x % y == 0:
                    dp[x] = min(dp[x], dp[y] + x / y)
        return dp[n]




