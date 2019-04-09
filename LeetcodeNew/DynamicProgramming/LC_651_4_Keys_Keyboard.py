
"""
https://www.jianshu.com/p/ee57e9ae02e5

Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys),
find out the maximum numbers of 'A' you can print on screen.

Example 1:
Input: N = 3
Output: 3
Explanation:
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A
Example 2:
Input: N = 7
Output: 9
Explanation:
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
Note:
1 <= N <= 50
Answers will be in the range of 32-bit signed integer.
"""

"""
First of all, we can know that if N < 7, then f[N] = N
since double current list length need 3 operations (ACP) and ACP must generate longer list than PPP for list with length > 3, the maximum for f[i] only have 3 choices:

1. from f[i - 3], by ACP total length : f[i - 3] * 2
2. from f[i - 4], by ACP + P total length : f[i - 4] * 3
3. from f[i - 5], by ACP + PP total length : f[i - 5] * 4
That's all. for i - 6 and smaller ACP + ACP longer than ACP + PPP. so we can get it from f[i - 3]
"""

"""
使用DP。

首先把 DP[ i ] 初始化为 i，代表的情形是不使用复制粘贴操作。然后将 j 从3开始一直到 i-1，
从3开始是为了确保至少有一个复制粘贴的操作。接着循环："以dp[1] 中的所有字符为基准之后全是粘贴操作" 
一直到 "以dp[i-3]中的所有字符为基准之后全是粘贴操作"。

比如:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
这里 n = 7 ，我们使用了 3 （j=4，i-j=7-4）步来获得 AAA
接着我们使用 4 步: Ctrl A, Ctrl C, Ctrl V, Ctrl V, 来获得j - 1 = 4 - 1 = 3 份 AAA 的复制。

我们要么一点不使用copy操作，就是我们初始化 DP[ i ] 为 i 的情形。要么使用copy操作，
这样我们要留3步给 Ctrl A, Ctrl C, Ctrl V ，所以 j 至少是 3.

得到公式 dp[ i ] = max ( dp[ i ] , dp[ i - j ] * ( j - 1 ) )      {  j in [ 3, i )  }
"""

"""
还有一种类似的想法。
使用 i 步来获得 maxA(i) ，然后用剩下的 n - i 步来获得 n - i - 1 个 maxA(i)的复制。

比如：
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
这里 n = 7 ，我们使用 i = 3 步来获得 AAA
接着我们使用剩下的 n - i = 4 步: Ctrl A, Ctrl C, Ctrl V, Ctrl V, 来获得 n - i - 1 = 3 个 AAA的复制。

如果我们不使用copy，那么答案就是 n, 或者我们使用copy，那么需要有3步来预留给 Ctrl A, Ctrl C, Ctrl V ，所以 i 最多为 n - 3。
"""
import collections

class Solution1:
    def maxA(self, N):

        f = [i for i in range(N+1)]
        for i in range(7, N+1):
            f[i] = max(f[i-3]*2, f[i-4]*3, f[i-5]*4)

        return f[N]


"""
DP using O(N^2) time and O(N) space

1. The key insight is that the optimal number will be generated using a sequence 'A', 
   followed by select+copy+paste, and then followed by a sequence of pastes.
2. Assume you are at x. select+copy+paste takes you to 2x in 3 strokes. 
   Now if you apply the three strokes again, you will reach 4x after 6 strokes. Instead, 
   if you used paste in strokes 4 to 6, you would have 5x. 
   This gives the intuition for optimal sequence.
3. The above insight naturally gives the DP algorithm. For example, when i = 7, 
   we can think of invoking select+copy+paste after 1,2,3,4 strokes. 
   Say j=3 with optimal value as dp[i], then we will have select+copy+paste+paste, which triples dp[i].
"""
class Solution2:
    def maxA(self, N):

        dp = [i for i in range(N+1)]
        for i in range(1,N+1):
            for j in range(1,i):
                if j+3<=i:
                    dp[i] = max(dp[i], dp[j]*(i-j-2) + dp[j])
        return dp[N]


"""
And the brilliant idea
classifying all possible routes into never copy
last few being paste, paste, paste...

You can do this becasue after the first paste, if you do another selectall, copy, 
that can count into following case, so the coverage is full.
"""
class Solution3:
    def maxA(self, N):
        DP = range(N + 1)
        for i in range(1, N + 1):
            for j in range(1, i - 3):
                DP[i] = max(DP[i], DP[j] * (i - j - 1))
        return DP[N]


"""
解题思路：
动态规划（Dynamic Programming）

dp[z][y]表示利用z次操作，缓冲区内的字符数为y时，屏幕上打印的最大字符数

初始dp[0][0] = 0

状态转移方程：

当按下字符A时：

dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + 1)

当按下Ctrl-V时：

dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + y)

当按下Ctrl-A + Ctrl-C时：

dp[z + 2][dp[z][y]] = max(dp[z + 2][dp[z][y]], dp[z][y])

"""

class Solution4:
    def maxA(self, N):

        dp = collections.defaultdict(lambda : collections.defaultdict(int))
        dp[0][0] = 0 #step, buffer
        for z in range(N):
            for y in dp[z]:
                #Key 1: (A):
                dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + 1)
                #Key 4: (Ctrl-V):
                dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + y)
                #Key 2: (Ctrl-A): + Key 3: (Ctrl-C):
                dp[z + 2][dp[z][y]] = max(dp[z + 2][dp[z][y]], dp[z][y])
        return max(dp[N].values())


