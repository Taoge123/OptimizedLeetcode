
"""
https://blog.csdn.net/fuxuemingzhu/article/details/83059602
https://www.jianshu.com/p/2104df9de5d5
https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116581/Detail-and-explanation-of-O(n)-solution-why-dpn2*dn-1%2Bdpn-3
https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116664/Schematic-explanation-of-two-equivalent-DP-recurrence-formula
https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116612/Easy-to-understand-O(n)-solution-with-Drawing-Picture-Explanation!
https://leetcode.com/problems/domino-and-tromino-tiling/solution/

We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

XX  <- domino

XX  <- "L" tromino
X
Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.

(In a tiling, every square must be covered by a tile.
Two tilings are different if and only if there are two 4-directionally adjacent cells on the board
such that exactly one of the tilings has both squares occupied by a tile.)

Example:
Input: 3
Output: 5
Explanation:
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY
"""
"""
when N==0, we need return 0, but in dp , we need make dp[0]=1 for easy to construct formula
dp[n]=dp[n-1]+dp[n-2]+ 2*(dp[n-3]+...+d[0])
=dp[n-1]+dp[n-2]+dp[n-3]+dp[n-3]+2*(dp[n-4]+...+d[0])
=dp[n-1]+dp[n-3]+(dp[n-2]+dp[n-3]+2*(dp[n-4]+...+d[0]))
=dp[n-1]+dp[n-3]+dp[n-1]
=2*dp[n-1]+dp[n-3]

 int numTilings(int N) {
    int md=1e9;
    md+=7;
    vector<long long> v(1001,0);
    v[1]=1;
    v[2]=2;
    v[3]=5;
    if(N<=3)
        return v[N];
    for(int i=4;i<=N;++i){
        v[i]=2*v[i-1]+v[i-3]; 
        v[i]%=md;
    }
    return v[N];
    
}
"""
"""
so the code can be write as this:

    int numTilings(int N) 
    {
        long long g[1001],u[1001];
        int mod=1000000007;
        g[0]=0; g[1]=1; g[2]=2;
        u[0]=0; u[1]=1; u[2]=2;
        
        for(int i=3;i<=N;i++)
        {
            u[i] = (u[i-1] + g[i-1]           )   %mod;
            g[i] = (g[i-1] + g[i-2] + 2*u[i-2])   %mod;
        }
        return g[N]%mod;
    }
"""
"""
10
lee215's avatar
lee215
13693
February 24, 2018 11:19 PM

2.3K VIEWS

The answer will be a recursive sequence as follow: 1, 1, 2, 5, 11, 24, 53, 117, 258, 569, 1255
It grows at a speed about 2 times bigger each time.
If you write down this recursive sequence and do some calculations, you may find that:

5 = 2 * 2 + 1
11 = 5 * 2 + 1
24 = 11 * 2 + 2
53 = 24 * 2 + 5
117 = 53 * 2 + 11
A[N] = A[N-1] * 2 + A[N-3]

Once you notice it, the rest work will be easy, even it may be hard to prove it.
"""

class SolutionLee2:
    def numTilings(self, N):
        a, b, c = 0, 1, 1
        for i in range(N - 1): a, b, c = b, c, (c + c + a) % int(1e9 + 7)
        return c


"""
3 simple steps to solve this problem:

Decide use dynamic programming.
Find dp equation.
Find initilization.
A[i] the number of tiling a 2*N-1 board, B[i] the number of tiling a 2*N board.
We can find this regular as .

A[i] = B[i - 2] + A[i - 1]
B[i] = B[i - 1] + B[i - 2] + A[i - 1] * 2
I also initialize B[0] = B[1] = 1, A[0] = A[1] = 0
"""

class SolutionLee1:
    def numTilings(self, N):
        A = [0] * (N + 1)
        B = [1, 1] + [0] * (N - 1)
        for i in range(2, N + 1):
            A[i] = (B[i - 2] + A[i - 1]) % int(1e9 + 7)
            B[i] = (B[i - 1] + B[i - 2] + A[i - 1] * 2) % int(1e9 + 7)
        return B[N]


"""

Result:

N =  0   1   2   3   4   5   6    7    8    9    10 ...
A = [0,  0,  1,  2,  4,  9, 20,  44,  97, 214,  472 ...
B = [1,  1,  2,  5, 11, 24, 53, 117, 258, 569, 1255 ...
This is in fact a double recursive sequence.
The code will be much simpler if you find out the regular for single recursive sequence.
"""

class Solution1:
    def numTilings(self, N):

        dp = [[0] * 2 for _ in range(N + 1)]
        dp[0][0] = 1
        dp[1][0] = 1
        for i in range(2, N + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + 2 * dp[i - 1][1]) % (10 ** 9 + 7)
            dp[i][1] = (dp[i - 2][0] + dp[i - 1][1]) % (10 ** 9 + 7)
        return dp[-1][0]



"""
题目大意：
有两种形状的多米诺骨牌（长条形和L形），骨牌可以旋转。

求拼成2xN的矩形的所有拼接方法的个数。

解题思路：
动态规划（Dynamic Programming）

dp[x][y]表示长度（两行的最小值）为x，末尾形状为y的拼接方法个数

y有三种可能：

0表示末尾没有多余部分

1表示第一行多出1个单元格

2表示第二行多出1个单元格
状态转移方程：

dp[x][0] = (dp[x - 1][0] + sum(dp[x - 2])) % MOD   1个竖条， 2个横条，L7， rotate(L7)

dp[x][1] = (dp[x - 1][0] + dp[x - 1][2]) % MOD    rotate(L)，L + 第一行横条

dp[x][2] = (dp[x - 1][0] + dp[x - 1][1]) % MOD    L，rotate(L) + 第二行横条
"""
class Solution2:
    def numTilings(self, N):

        MOD = 10**9 + 7
        dp = [[0] * 3 for x in range(N + 10)]
        dp[0] = [1, 0, 0]
        dp[1] = [1, 1, 1]
        for x in range(2, N + 1):
            dp[x][0] = (dp[x - 1][0] + sum(dp[x - 2])) % MOD
            dp[x][1] = (dp[x - 1][0] + dp[x - 1][2]) % MOD
            dp[x][2] = (dp[x - 1][0] + dp[x - 1][1]) % MOD
        return dp[N][0]



