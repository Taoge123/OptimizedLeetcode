
"""
https://leetcode.com/problems/knight-dialer/discuss/189252/O(logN)
https://buptwc.com/2018/11/05/leetcode-935-Knight-Dialer/
https://leetcode.com/problems/knight-dialer/discuss/212801/Python-two-methods%3A-DP-and-Markov-Chain
https://blog.csdn.net/fuxuemingzhu/article/details/83716573
https://www.cnblogs.com/seyjs/p/9911142.html


935. Knight Dialer
Medium

164

43

Favorite

Share
A chess knight can move as indicated in the chess diagram below:

This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.

Example 1:

Input: 1
Output: 10
Example 2:

Input: 2
Output: 20
Example 3:

Input: 3
Output: 46


Note:

1 <= N <= 5000
"""
"""
Naive recursion:
O(N) time and O(1) space, good enough.
"""
import numpy as np
class SolutionLee:
    def knightDialer(self, N):
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        for i in range(N - 1):
            x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = \
                x6 + x8, x7 + x9, x4 + x8, \
                x3 + x9 + x0, 0, x1 + x7 + x0, \
                x2 + x6, x1 + x3, x2 + x4, \
                x4 + x6
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10**9 + 7)


"""
In fact, we recursively did pow operation.
This can be optimised to O(log) time.

Construct a 10 * 10 transformation matrix M.
M[i][j] = 1 if i and j is connnected.

if N = 1, return 10.
if N > 1, return sum of [1,1,1,1,1,1,1,1,1,1] * M ^ (N - 1)

The power of matrix reveals the number of walks in an undirected graph.
Find more details on this link provide by @shankark:
https://math.stackexchange.com/questions/1890620/finding-path-lengths-by-the-power-of-adjacency-matrix-of-an-undirected-graph
"""

class Solution2:
    def knightDialer(self, N):
        mod = 10**9 + 7
        if N == 1: return 10
        M = np.matrix([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])
        res, N = 1, N - 1
        while N:
            if N % 2: res = res * M % mod
            M = M * M % mod
            N /= 2
        return int(np.sum(res)) % mod



"""
这一次，我们将 “骑士” 放在电话拨号盘的任意数字键（如上图所示）上，接下来，骑士将会跳 N-1 步。
每一步必须是从一个数字键跳到另一个数字键。
每当它落在一个键上（包括骑士的初始位置），都会拨出键所对应的数字，总共按下 N 位数字。

你能用这种方式拨出多少个不同的号码？
因为答案可能很大，所以输出答案模 10^9 + 7。

题意分析：
一个骑士在电话拨号盘上连续行走N次，求总共可能走出多少种不同的电话。

tips：看到mod 1e9+7，就要想到dp

思路分析：
我认为这道题当你往dp方面去想的时候，就变得很简单，因为dp定义和递推式都显而易见。
定义dp[i][j]表示现在处于i位置，继续走j步所能走出的不同电话数量。
那么有dp[i][j] = sum(dp[nex][j-1] for nex in (i能走到的位置) )

使用一个字典d来保存每个位置所能到达的下一个位置。
初始化所有的dp[i][0] = 1，因为不能继续走，所以只有1种可能。
"""
class Solution3:
    def knightDialer(self, N):
        d = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3],
             9: [2, 4]}
        dp = [[0] * 10 for _ in range(N)]
        mod = 10 ** 9 + 7
        for i in range(10): dp[0][i] = 1

        for i in range(1, N):
            for j in range(10):
                for nex in d[j]:
                    dp[i][j] += dp[i - 1][nex]
                dp[i][j] %= mod

        return sum(dp[N - 1]) % mod


"""
解题思路：很明显的动态规划的场景。首先我们可以维护如下的一个映射字典:key为到达的数字，
value为可以由哪些数字经过一次跳跃到达key的数字。接下来假设dp[i][j] 为经过跳跃i次并且最后一次跳跃的终点是j，
那么有dp[i][j] = dp[i-1][dic[j][0]] + dp[i-1][dic[j][1]] + ... dp[i-1][dic[j][n]]。
最终的结果就是dp[N][0] + dp[N][1] + ... dp[N][9]。后来经过测试发现，这种解法会超时，
因为题目约定了N最大是5000，因此可以事先计算出1~5000的所有结果缓存起来

　　　　 dic[1] = [6,8]
        dic[2] = [7,9]
        dic[3] = [4,8]
        dic[4] = [3,9,0]
        dic[5] = []
        dic[6] = [1,7,0]
        dic[7] = [2,6]
        dic[8] = [1,3]
        dic[9] = [2,4]
        dic[0] = [4,6]
"""

class Solution4:
    res = []
    def knightDialer(self, N):

        if len(self.res) != 0:
            return self.res[N-1]
        dic = {}
        dic[1] = [6,8]
        dic[2] = [7,9]
        dic[3] = [4,8]
        dic[4] = [3,9,0]
        dic[5] = []
        dic[6] = [1,7,0]
        dic[7] = [2,6]
        dic[8] = [1,3]
        dic[9] = [2,4]
        dic[0] = [4,6]
        dp = []
        for i in range(5001):
            if i == 0:
                tl = [1] * 10
            else:
                tl = [0] * 10
            dp.append(tl)
        for i in range(5001):
            for j in range(10):
                for k in dic[j]:
                    dp[i][j] += dp[i-1][k]
        for i in range(5001):
            self.res.append(sum(dp[i]) % (pow(10,9) + 7))
        return self.res[N-1]





