
"""
http://www.noteanddata.com/leetcode-920-Number-of-Music-Playlists-solution-note.html
https://leetcode.com/problems/number-of-music-playlists/solution/
http://massivealgorithms.blogspot.com/2018/11/leetcode-920-number-of-music-playlists.html

dp[i][j] = dp[i-1][j] * Math.max(j-K, 0) + dp[i-1][j-1] * (N-j+1)


Your music player contains N different songs and she wants to listen to L (not necessarily different) songs during your trip.
You create a playlist so that:

Every song is played at least once
A song can only be played again only if K other songs have been played
Return the number of possible playlists.  As the answer can be very large, return it modulo 10^9 + 7.



Example 1:

Input: N = 3, L = 3, K = 1
Output: 6
Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
Example 2:

Input: N = 2, L = 3, K = 0
Output: 6
Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]
Example 3:

Input: N = 2, L = 3, K = 1
Output: 2
Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]


Note:

0 <= K < N <= L <= 100

你的音乐播放器里有 N 首不同的歌，在旅途中，你的旅伴想要听 L 首歌（不一定不同，即允许歌曲重复）。请你为她按如下规则创建一个播放列表：
每首歌至少播放一次。
一首歌只有在其他 K 首歌播放完之后才能再次播放。
返回可以满足要求的播放列表的数量。由于答案可能非常大，请返回它模 10^9 + 7 的结果。

示例 1：
输入：N = 3, L = 3, K = 1
输出：6
解释：有 6 种可能的播放列表。[1, 2, 3]，[1, 3, 2]，[2, 1, 3]，[2, 3, 1]，[3, 1, 2]，[3, 2, 1].

示例 2：
输入：N = 2, L = 3, K = 0
输出：6
解释：有 6 种可能的播放列表。[1, 1, 2]，[1, 2, 1]，[2, 1, 1]，[2, 2, 1]，[2, 1, 2]，[1, 2, 2]

示例 3：
输入：N = 2, L = 3, K = 1
输出：2
解释：有 2 种可能的播放列表。[1, 2, 1]，[2, 1, 2]

提示：

0 <= K < N <= L <= 100

"""
"""
题意分析：
总共有n首歌，要听l首歌，必须每首歌至少听一遍，若某一首歌需要听多遍的话，其中间的歌曲数量至少为k首。

思路分析：
在我的很多文中都提到过，看到mod 10^9+7，一定第一时间要想到dp。不说这种题目百分之百是dp，起码在leetcode上的题目基本全是。

那么怎么去分析呢？这道题一看像一个排列组合问题，熟悉排列组合的人对下面这个式子肯定不陌生

这个式子可以这样描述，在n个人里面挑选m个人，我们从挑不挑得到某个特定人X来考虑。
若挑得到，那么我们从剩下的n-1个人中再挑m-1个人。
若挑不到，那么我们从剩下的n-1个人中挑m个人。

这道题也是用类似的思路，我们定义f(n,l,k)为题目所求，则有：
f(n,l,k) = f(n-1,l-1,k) \* n + f(n,l-1,k) \* (n-k)
其中f(n-1,l-1,k)代表某个特定的歌只最后出现一次，其余n-1首歌填充了前面l-1个位置，因为有n首不同的歌所以乘n。
f(n,l-1,k)代表最后出现的某个特定的歌前面已经出现过了，这个最后出现的歌和当前最后k个位置的歌应当不相同，故乘(n-k)。

递推式已经找到，那么初始状态是什么呢？
显然当n==l时，则就是一个全排列，即为n!
当n > l or k > n时，都不存在解，故为0

注意到在递推式中k其实始终无变化，所以实际定义dp时k可以省去
"""
import math


class Solution1:
    def numMusicPlaylists(self, n, l, k):
        mod = 10**9 + 7
        # fib[n-1] = n!
        fib = list(range(1,101))
        for i in range(1, len(fib)):
            fib[i] *= fib[i-1]

        dp = [[0]*(l+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(i,l+1):
                if i == j:
                    dp[i][j] = fib[i-1]
                elif i < k:
                    continue # 关键，否则(i-k) < 0
                else:
                    dp[i][j] = dp[i-1][j-1] * i + dp[i][j-1] * (i-k)
        return dp[-1][-1] % mod


"""
F(N,L,K) = F(N - 1, L - 1, K) * N + F(N, L - 1, K) * (N - K)

F(N - 1, L - 1, K)
If only N - 1 in the L - 1 first songs.
We need to put the rest one at the end of music list.
Any song can be this last song, so there are N possible combinations.

F(N, L - 1, K)
If already N in the L - 1 first songs.
We can put any song at the end of music list,
but it should be different from K last song.
We have N - K choices.

Time Complexity:
O((L-K)(N-K))
"""

class SolutionLee:
    def numMusicPlaylists(self, N, L, K):
        dp = [[0 for i in range(L + 1)] for j in range(N + 1)]
        for i in range(K + 1, N + 1):
            for j in range(i, L + 1):
                if i == j or i == K + 1:
                    dp[i][j] = math.factorial(i)
                else:
                    dp[i][j] = dp[i - 1][j - 1] * i + dp[i][j - 1] * (i - K)
        return dp[N][L] % (10**9 + 7)


"""
I like this post because it describes a function. To come up with the solution 
it's useful to think in terms of pure declarative functions, 
not in terms of imperative dp table updates. It's useful not only for this problem, but for all dp problems. 
Pure functional recursion is like "source code", loops over dp table is the "output" of optimizing translator.

To understand recursion of this problem, let's consider simplified problems first.

Simplified problem 1
Get nr of ways to build playlist of length L out of N distinct songs. The formula is trivial:

F1(N, L) = 
   1, if L=0  // base case, one way to build empty playlist
   F1(N, L-1) * N  // ways to build prefix times ways to choose last song
   
   
Simplified problem 2
Let's add constraint that every song has to be played once. 
F2(N, L) - nr of ways to build playlist of length L out of N distinct songs with guarantee 
that each distinct song is played at least once.
How do we implement the constraint? We have to introduce new songs at some points. 
Instead of thinking about all N songs, let's think about one new song 
and delegate the rest to F2(N-1, ...). At the point we introduce a new song, 
we are bound to have valid playlist prefix that does not contain this song 
and that is one song shorter. By definition of F2(N, L), nr of ways to build such prefix is F2(N-1, L-1) 
and there are N ways to chose a new song, hence F2(N-1, L-1) * N term. 
Note that F2(N-1, ...) does not mean we build playlist out of first N-1 songs in some ordered list 1,2,3,...,N-1. 
F2(N-1, ...) means we use N-1 distinct songs without specifying which ones.
We can not simply declare that F2(N, L) = F2(N-1, L-1) * N, 
because introduction of new song is not the only way to have playlist N,L. 
We can also have playlist prefix that already introduced all N songs, 
and we play one of those, hence F2(N, L-1) * N term.
   
F2(N, L)
   0, if (L=0) != (N=0)  // base case 2. One param is zero, the other is not. 
                         // No way to build empty list and use N>0 songs at least once. 
                         // No way to build L>0 list out of 0 songs.
   1, if L=0 and N=0  // base case 1, there exists one way to build empty playlist
   F2(N-1, L-1)*N  +  F2(N, L-1, K)*N
   
Original problem
Let's add constraint about no reusing of last K songs. 
F3(N, L, K) - nr of ways to build playlist of length L out of N distinct songs with guarantee 
that each distinct song is played at least once and individual song is used again only when K other songs played.
That's relatively easy. K limits the choice of the song to reuse in the second term 
F2(N, L-1, K) * N -> F2(N, L-1, K) * (N-K). When playlist is shorter than K (N-K<0), 
there is no way to reuse songs and second term should be zeroed.

F3(N,L,K)
   0, if (L=0) != (N=0)  // base case 2. One param is zero, the other is not. No way to build empty list and use N>0 songs at least once. No way to build L>0 list out of 0 songs.
   1, if L=0 and N=0  // base case 1, there exists one way to build empty playlist
   F2(N-1, L-1, K)*N  +  F2(N, L-1, K)*max(0, N-K)

Exponential recursion

int numMusicPlaylists(const int N, const int L, const int K) {
    function<int(const int n /* nr of songs */, const int l /* playlist len */)> dp;
    dp = [K, &dp](const int n, const int l) {
        if ((l == 0) != (n == 0)) {
            return 0;
        } else if (l == 0 && n == 0) {
            return 1;
        } else {
            return
                dp(n-1, l-1) * n + 
                dp(n, l-1) * max(0, n-K);
        }
    };
    return dp(N, L);
}


Polynomial but unreadable bottomup

int numMusicPlaylists(const int N, const int L, const int K) {
    const long mod = 1e9 + 7;
    vector<long> memo(N + 1);
    memo[0] = 1;
    for (int l = 1; l <= L; ++l) {
        for (int n = min(N, l); n > 0; --n) {
            memo[n] = (memo[n-1] * n + memo[n] * max(0, n-K)) % mod;
        }
        memo[0] = 0;
    }
    return memo[N];
}

"""
"""
My understanding of the initial values in the dp array.

1. Why dp[0][0] = 1?
    For dp[1][1], we can fit a size 1 list with 1 new song, so it's dp[0][1 - 1] * (N - (1 - 1)) = 1 * N.
    And all j > i are invalid cases (you can't put more songs to an empty list), so for j > 0, dp[0][j] = 0.
    This rule also applies to remaining rows, e.g. for j > 1, dp[1][j] are also 0.
2. Why dp[i][0] is 0 for i > 0?
    For i > 1, since there is no way to fill a non-empty list with 0 songs, the j = 0 case is always 0.
"""

"""
dp[i][j] denotes the solution of i songs with j different songs. So the final answer should be dp[L][N]

Think one step before the last one, there are only cases for the answer of dp[i][j]
case 1 (the last added one is new song): listen i - 1 songs with j - 1 different songs, then the last one is definitely new song with the choices of N - (j - 1).
Case 2 (the last added one is old song): listen i - 1 songs with j different songs, then the last one is definitely old song with the choices of j
if without the constraint of K, the status equation will be
dp[i][j] = dp[i-1][j-1] * (N - (j-1)) + dp[i-1][j] * j

If with the constaint of K, there are also two cases
Case 1: no changes since the last added one is new song. Hence, there is no conflict
Case 2: now we don't have choices of j for the last added old song. It should be updated j - k because k songs can't be chosed from j - 1 to j - k. However, if j <= K, this case will be 0 because only after choosing K different other songs, old song can be chosen.

if (j > k)
dp[i][j] = dp[i-1][j-1] * (N- (j-1)) + dp[i-1][j] * (j-k)
else
dp[i][j] = dp[i-1][j-1] * (N- (j-1))

"""

"""
思路

思路参考了清华大学计算机系算协比赛部的思路LeetCode周赛#105题解。动态规划。

dp[i][j] = 用j首不同的歌产生长度为i的歌单的种数

dp[i][j] = dp[i-1][j-1]*(N-(j-1))// 第i首歌不是前(j-1)首歌中的某一首歌

            + dp[i-1][j]*(j-K)  // 第i首歌是前j首歌中的某一首歌，与第(i-K):(i-1)首歌不同

边界条件: dp[0][0] = 1
"""

"""
分析
这个优化问题，求最多的可能性，需要用动态规划做，
这里有三个变量， 状态比较复杂，但是可以固定N，始终在N首曲子里面选择。
设置动态规划数组dp[i][j], 表示第i个位置，在N首歌曲里面，放了j首不同的歌曲的个数， 并且符合K的条件
那么dp[L][N]就是有L个位置，放了N首不同的歌曲的结果。

那么，寻找递归关系， 对于dp[i][j], 递归关系一定是寻找和i-1的关系， 因为第i个位置还没有放歌曲，
这时候，有两种情况，
a. 如果第i首曲子是之前没有放过的，那前一项就应该是dp[i-1][j-1], 然后这个时候可以选择的曲子是
N-(j-1), 所以那么这时候的可能性是dp[i-1][j-1] * (N-(j-1))
b. 如果第i首曲子是之前放过的，那么前一项就是dp[i-1][j], 这时候可以选择的曲子的范围是多少呢？
因为要符合K的要求，那最近的这K个就不能选择了，所以是j-K个， 当然因为j-K有可能小于0， 所以要取Math.max(j-K, 0)

c. 对于b的情况这里可能会有个疑问，是不是最近这K个不选了以后一定是对的？有没有可能j-K前面的若干个里面会和最近的K个有冲突？
我当时就有这个疑问，其实是这样， 对于dp[i-1][j]
其实是这样， 这里最近的这K个曲子，因为已经符合要求了，所以最近的这K个曲子就一定是不重复的。
然后这里选择的是j-K, 而不是i-K,
所以是j首不同的曲子里面，去掉K首最近被用过的（一定是不重复的），这样剩下的曲子一定不会在最近的K个位置里面有冲突。

d. 综合a和b两种情况， 得出递推公式：
dp[i][j] = dp[i-1][j] * Math.max(j-K, 0) + dp[i-1][j-1] * (N-j+1)

e. 边界条件
这里主要的边界条件是i=1和j=1的情况，
if i < j, dp[i][j] = 0, 因为只有i个位置， 但是要放j首不同的曲子， 这个肯定不可能。
dp[1][1] = N, 因为1个位置， 从N首不同的曲子里面选择1首曲子， 那就有N种可能。
if i > 1 && j ==1
这时候分两种情况， 如果K=0， 那么就是在N首曲子里面选一首，然后填满i个位置，就有N个选择，
如果K > 0, dp[i][1] = 0， 因为只有一首曲子，但是要符合K的条件，已经不可能了。
"""
"""
代码2
实际上，后面测试了一些，只要设置了dp[1][1] = N以后，就可以直接进入递推模式了，
dp[i][1] 和dp[1][j] 就已经在递推中完全完成了。
因为所有的dp[0][j] = 0, 所以对于j > 1, 所有的dp[1][j] = 0
而对dp[i][1], 也就是j= 1, 如果i > 1的话， 因为dp[i-1][0] 都是0，
而如果K = 0, Math.max(j-K, 0)= 1, 所以dp[i][1] = N,
如果K >= 1, Math.max(j-K, 0) = 0,所以整个递推关系是完全成立的。
"""








