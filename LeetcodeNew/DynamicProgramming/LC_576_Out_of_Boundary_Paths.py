
"""

dp[t + 1][x + dx][y + dy] += dp[t][x][y]


There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball,
you can move the ball to adjacent cell or cross the grid boundary
in four directions (up, down, left, right). However, you can at most move N times.
Find out the number of paths to move the ball out of grid boundary.
The answer may be very large, return it after mod 109 + 7.

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

Note:

Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
"""

"""
Approach #2 Recursion with memoization [Accepted]
Algorithm

In the brute force approach, while going through the various branches of the recursion tree, 
we could reach the same position with the same number of moves left.

Thus, a lot of redundant function calls are made with the same set of parameters leading to a useless increase in runtime. 
We can remove this redundancy by making use of a memoization array, memomemo. 
memo[i][j][k]memo[i][j][k] is used to store the number of possible moves leading to a path out of the boundary 
if the current position is given by the indices (i, j)(i,j) and number of moves left is kk.

Thus, now if a function call with some parameters is repeated, 
the memomemo array will already contain valid values corresponding to that function call resulting in pruning of the search space.

Complexity Analysis

Time complexity : O(m*n*N)O(m∗n∗N). We need to fill the memomemo array once with dimensions mmxnnxNN. 
Here, mm, nn refer to the number of rows and columns of the given grid respectively. 
NN refers to the total number of allowed moves.

Space complexity : O(m*n*N)O(m∗n∗N). memomemo array of size m*n*Nm∗n∗N is used.
"""

"""
Approach #3 Dynamic Programming [Accepted]
Algorithm

The idea behind this approach is that if we can reach some position in xx moves, 
we can reach all its adjacent positions in x+1x+1 moves. Based on this idea, 
we make use of a 2-D dpdp array to store the number of ways in which a particular position can be reached. 
dp[i][j]dp[i][j] refers to the number of ways the position corresponding to the indices (i,j)(i,j) can be reached given some particular number of moves.

Now, if the current dpdp array stores the number of ways the various positions can be reached by making use of x-1x−1 moves, 
in order to determine the number of ways the position (i,j)(i,j) can be reached by making use of xx moves, 
we need to update the corresponding dpdp entry 
as dp[i][j] = dp[i-1][j] + dp[i+1][j] + dp[i][j-1] + dp[i][j+1]dp[i][j]=dp[i−1][j]+dp[i+1][j]+dp[i][j−1]+dp[i][j+1] 
taking care of boundary conditions. 
This happens because we can reach the index (i,j)(i,j) from any of the four adjacent positions 
and the total number of ways of reaching the index (i,j)(i,j) 
in xx moves is the sum of the ways of reaching the adjacent positions in x-1x−1 moves.

But, if we alter the dpdp array, now some of the entries will correspond to x-1x−1 moves 
and the updated ones will correspond to xx moves. Thus, we need to find a way to tackle this issue. 
So, instead of updating the dpdp array for the current(xx) moves, 
we make use of a temporary 2-D array temptemp to store the updated results for xx moves, 
making use of the results obtained for dpdp array corresponding to x-1x−1 moves. 
After all the entries for all the positions have been considered for xx moves, 
we update the dpdp array based on temptemp. Thus, dpdp now contains the entries corresponding to xx moves.

Thus, we start off by considering zero move available for which we make an initial entry of 
dp[x][y] = 1dp[x][y]=1((x,y)(x,y) is the initial position), 
since we can reach only this position in zero move. 
Then, we increase the number of moves to 1 and update all the dpdp entries appropriately. 
We do so for all the moves possible from 1 to N.

In order to update countcount, which indicates the total number of possible moves which lead an out of boundary path, 
we need to perform the update only when we reach the boundary. 
We update the count as count = count + dp[i][j]count=count+dp[i][j], 
where (i,j)(i,j) corresponds to one of the boundaries. But, if (i,j)(i,j) is simultaneously a part of multiple boundaries, 
we need to add the dp[i][j]dp[i][j] factor multiple times(same as the number of boundaries to which (i,j)(i,j) belongs).

After we are done with all the NN moves, countcount gives the required result.

The following animation illustrates the process:
"""


"""
At time t, let's maintain cur[r][c] = the number of paths to (r, c) with t moves, 
and nxt[r][c] = the number of paths to (r, c) with t+1 moves.

A ball at (r, c) at time t, can move in one of four directions. 
If it stays on the board, then it contributes to a path that takes t+1 moves. 
If it falls off the board, then it contributes to the final answer.
"""
import collections

class Solution1:
    def findPaths(self, R, C, N, sr, sc):
        MOD = 10 ** 9 + 7
        nxt = [[0] * C for _ in range(R)]
        nxt[sr][sc] = 1

        ans = 0
        for time in range(N):
            cur = nxt
            nxt = [[0] * C for _ in range(R)]
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < R and 0 <= nc < C:
                            nxt[nr][nc] += val
                            nxt[nr][nc] %= MOD
                        else:
                            ans += val
                            ans %= MOD

        return ans


"""
说明:

球一旦出界，就不能再被移动回网格内。
网格的长度和高度在 [1,50] 的范围内。
N 在 [0,50] 的范围内。
分析：

这道题乍一看很像一个标准的bfs，因为限定最多只能移动N次，我们只要bfs依次遍历发现出界就+1，当bfs的深度大于N的时候break。
当然理论上是没有任何问题的，确实能得出正确答案，但是这里N的取值范围达到了50，我们对任意一个点bfs有四个方向（可以走回头路），
那么复杂度达到了4^N，显然会超时。当然我会在文章后面给出bfs的做法，毕竟这是可以处理N比较小的情况的解法，让大家更熟悉bfs的套路。

我不知道你们有没有这种感觉，一般看到这个mod 1e9+7，这道题8成就是dp了，
而且就是那种每个dp值你都得mod一下再去进行运算的那种。我觉得这算一个小技巧吧，看到mod 1e9+7就要想到dp。
显然，这里dp很好定义，我们定义dp[(i,j,N)]表示从i,j出发，最多走N步情况下满足题意的路径数量，
那么我们所求也就是dp[(i,j,N)]。根据我们上面说的bfs的思路，递推式可得：

dp[(i,j,N)] = dp[(i+1,j,N-1)] 
            + dp[(i-1,j,N-1)] 
            + dp[(i,j+1,N-1)] 
            + dp[(i,j-1,N-1)]

思路：

处理好边界情况：
当i,j仍然在网格内时，如果N=0，说明这条路走不出去,dp[(i,j,N)] = 0
当i,j仍然在网格内时，如果N>0，如递推式
当i,j在网格外时，说明已经走出去，dp[(i,j,N)] = 1
这里我为了方便代码书写就用的记忆化的形式，用一个cache来存储已经计算过的结果
"""
class Solution2:
    def findPaths(self, m, n, N, i, j):
        mod = 10**9 + 7
        cache = collections.defaultdict(int)
        def helper(i,j,N):
            # 记忆化思想
            if (i,j,N) in cache:
                return cache[(i,j,N)]
            #i,j在网格内情况
            if 0<=i<m and 0<=j<n:
                if N == 0:
                    cache[(i,j,N)] = 0
                    return cache[(i,j,N)]

                for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    cache[(i,j,N)] += helper(x,y,N-1)
                return cache[(i,j,N)] % mod
            # 网格外情况
            else:
                cache[(i,j,N)] = 1
                return cache[(i,j,N)]
        return helper(i,j,N) % mod


class SolutionBFSTLE:
    def findPaths(m, n, N, i, j):
        mod = 10 ** 9 + 7
        Q = collections.deque([(i, j, 0)])
        res = 0
        while Q:
            x, y, step = Q.popleft()
            if step > N: break
            if 0 <= x < m and 0 <= y < n:
                Q.append((x + 1, y, step + 1))
                Q.append((x - 1, y, step + 1))
                Q.append((x, y + 1, step + 1))
                Q.append((x, y - 1, step + 1))
            else:
                res += 1
        return res % mod


class SolutinLee:
    def findPaths(self, m, n, N, x, y):
        M = [[0 for i in range(n)] for j in range(m)]
        for _ in range(N):
            M = [[(i == 0 or M[i - 1][j]) + (i + 1 == m or M[i + 1][j])
                  + (j == 0 or M[i][j - 1]) + (j + 1 == n or M[i][j + 1])
                  for j in range(n)] for i in range(m)]
        return M[x][y] % (10 ** 9 + 7)


# Make it 1-line:
class SolutionLee2:
    def findPaths(self, m, n, N, x, y):
        return reduce(lambda M, _:
                      [[(i == 0 or M[i - 1][j]) + (i + 1 == m or M[i + 1][j])
                        + (j == 0 or M[i][j - 1]) + (j + 1 == n or M[i][j + 1])
                        for j in range(n)] for i in range(m)], range(N),
                      [[0 for i in range(n)] for j in range(m)])[x][y] % (10 ** 9 + 7)



class Solution3:
    def findPaths(self, m, n, N, i, j):

        memo = {}
        def helper(N, i, j):
            if (N, i, j) in memo: return memo[(N, i, j)]
            if N == 0: return 0
            ans = 0
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if i + x >= 0 and i + x < m and j + y >= 0 and j + y < n:
                    ans += helper(N - 1, i + x, j + y)
                else:
                    ans += 1
            memo[(N, i, j)] = ans
            return ans
        return helper(N, i, j) % (10**9 + 7)


class Solution4:
    def findPaths(self, m, n, N, i, j):
        d = [[[-1] * n for _ in range(m)] for _ in range(N + 1)]
        def dfs(N, i, j, d):
            if i in [-1, m] or j in [-1, n]:
                return 1
            if N == 0:
                return 0
            if d[N][i][j] != -1:
                return d[N][i][j]
            d[N][i][j] = dfs(N - 1, i - 1, j, d) + dfs(N - 1, i + 1, j, d) + dfs(N - 1, i, j - 1, d) + dfs(N - 1,i, j + 1, d)
            return d[N][i][j] % (10**9 + 7)
        return dfs(N, i, j, d)

"""
We can define the state of this problem as (i, j, n), where (i, j) is the current position 
in the grid and n is the step count available at present.

For a given input state (i, j, n), we can count its oob paths by counting the paths 
of its adjacent positions (with n-1) recursivelly until the i or j out of boundary.

It's a pattern for which the memoization-based DP (i.e. top-down DP) can be used.

NOTE: the bulit-in library functools.lru_cache is a more memory-efficient choice for caching the dp states.
"""


class Solution5:
    def findPaths(self, m, n, N, i, j):
        self._memo = {}
        res = self._dfs(m, n, N, i, j)
        upper = int(1e9 + 7)
        return res % upper

    def _dfs(self, m, n, N, i, j):
        if N < 1:
            return 0

        if i >= N and j >= N and (m - 1 - i) >= N and (n - 1 - j) >= N:
            return 0

        if (i, j, N) not in self._memo:
            res = 0
            res += 1 if i == 0 else self._dfs(m, n, N - 1, i - 1, j)
            res += 1 if i == m - 1 else self._dfs(m, n, N - 1, i + 1, j)
            res += 1 if j == 0 else self._dfs(m, n, N - 1, i, j - 1)
            res += 1 if j == n - 1 else self._dfs(m, n, N - 1, i, j + 1)
            self._memo[i, j, N] = res
        return self._memo[i, j, N]


"""
题目大意
每次可以把足球从一个格子移动到另一个格子，要求最多通过N步能使得球移动到外边的方案数？

解题方法
动态规划
这个题有个很明显的对于动态规划的提示，那就是要模10^9 + 7，也就是说结果会很大，普通的搜索可能hold不住。

使用三维数组dp[k][x][y]表示在不超过k步的情况下，从x,y点移动到外边需要的步数。
那么，当前位置通过k步移动到外边的步数等于其周围4个位置走k - 1步移动到外边的步数和。

因为当x,y处于边界的时候，实际上只有两个或者三个相邻的位置，因为向边界方向走的话，只需要1步就可以移动到外部。
所以，如果向当前位置的周围位置出界的话，那么从这个方向需要出去移动步数就是1.

最后求和取模。

时间复杂度是O(Nmn)，空间复杂度是O(Nmn).
"""

class Solution11:
    def findPaths(self, m, n, N, i, j):

        dp = [[[0] * n for _ in range(m)] for _ in range(N + 1)]
        for s in range(1, N + 1):
            for x in range(m):
                for y in range(n):
                    v1 = 1 if x == 0 else dp[s - 1][x - 1][y]
                    v2 = 1 if x == m - 1 else dp[s - 1][x + 1][y]
                    v3 = 1 if y == 0 else dp[s - 1][x][y - 1]
                    v4 = 1 if y == n - 1 else dp[s - 1][x][y + 1]
                    dp[s][x][y] = (v1 + v2 + v3 + v4) % (10**9 + 7)
        return dp[N][i][j]


"""
上面这个做法可以看出每个状态其实只和上一次的状态有关，因此可以做状态压缩节省空间。

只使用二维数组表示地图即可，需要注意的是每次循环的时候还是需要重新开一个全部为0的curStatus，
为什么全部是0而不是dp的拷贝呢？因为我们每次对下一次的状态进行搜索之前，下个状态应该全部是未知的，
我们下面的代码就是计算每个位置的值，因此不能初始化dp的拷贝，否则下面的代码不work。其实这个和上面的做法对比一下就知道了，
因为上面的做法中，每一步开始的时候，里面的二维数组其实全部都是0.

每次搜索结束之后，需要更新dp，也就是我们把当前的状态作为下次搜索的初始状态。

时间复杂度是O(Nmn)，空间复杂度是O(m*n).
"""
class Solution22:
    def findPaths(self, m, n, N, i, j):

        dp = [[0] * n for _ in range(m)]
        for s in range(1, N + 1):
            curStatus = [[0] * n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    v1 = 1 if x == 0 else dp[x - 1][y]
                    v2 = 1 if x == m - 1 else dp[x + 1][y]
                    v3 = 1 if y == 0 else dp[x][y - 1]
                    v4 = 1 if y == n - 1 else dp[x][y + 1]
                    curStatus[x][y] = (v1 + v2 + v3 + v4) % (10**9 + 7)
            dp = curStatus
        return dp[i][j]


"""
状态搜索
这个dp其实属于对状态的搜索，如果看了《计算机考研机试指南》或者《挑战程序设计竞赛》的话，
会很清楚的知道其实这是个搜索的题目。归根到底都是对状态的转移问题，所以这个方法的名称叫做动归还是搜索都可以。

这种的做法有点类似于BFS搜索的题目，我们在做BFS的时候也会记录当前处于哪一步，所以是非常类似的。
我们定义了四个搜索的方向，从当前位置向周围4个方向进行搜索，如果搜索到了边界以外，和上面的做法类似的，我们把当前的步数+1；
如果在边界以内，那么就把当前第s步的结果增加第s-1步的(nx, ny)位置能到达边界的解法步数。

时间复杂度是O(Nmn)，空间复杂度是O(Nmn).
"""

class Solution33:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[[0] * n for _ in range(m)] for _ in range(N + 1)]
        ds = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for s in range(1, N + 1):
            for x in range(m):
                for y in range(n):
                    for d in ds:
                        nx, ny = x + d[0], y + d[1]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            dp[s][x][y] += 1
                        else:
                            dp[s][x][y] = (dp[s][x][y] + dp[s - 1][nx][ny]) % (10**9 + 7)
        return dp[N][i][j]

"""
同样的可以优化空间。

时间复杂度是O(Nmn)，空间复杂度是O(m*n).
"""
class Solution44:
    def findPaths(self, m, n, N, i, j):

        dp = [[0] * n for _ in range(m)]
        ds = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for s in range(1, N + 1):
            curStatus = [[0] * n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    for d in ds:
                        nx, ny = x + d[0], y + d[1]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            curStatus[x][y] += 1
                        else:
                            curStatus[x][y] = (curStatus[x][y] + dp[nx][ny]) % (10**9 + 7)
            dp = curStatus
        return dp[i][j]

"""
记忆化搜索
其实，应该是先有了记忆化搜索的代码才能推出dp。这个题我用记忆化搜索重新实现了一下，但是发现果然过不了啊！
但是记忆化搜索确实能加深我们对这个题目的理解。

把上面的状态搜索的dp改成记忆化搜索后的代码如下。如何加深理解呢？看看dfs的参数，变量其实只有x,y两个。
dfs函数代表了我们从(x, y)位置出发，最多移动N次的情况下能到达边界的个数。所以，我们的(x, y)的初始化值是题目要求的(i, j).

最后TLE了，很无奈，因为C++版本的能够通过。

时间复杂度是O(Nmn)，空间复杂度是O(Nmn).
"""

"""
解题思路：
动态规划（Dynamic Programming）

数组dp[t][x][y]表示第t次移动时，坐标x, y处的移动路径总数。

状态转移方程：

dp[t + 1][x + dx][y + dy] += dp[t][x][y]    

其中t表示移动的次数，dx, dy 取值 (1,0), (-1,0), (0,1), (0,-1)
当x + dx或者y + dy超出边界时，将结果累加至最终答案。
"""
class Solution55:
    def findPaths(self, m, n, N, i, j):

        MOD = 10**9 + 7
        dz = zip((1, 0, -1, 0), (0, 1, 0, -1))
        dp = [[0] *n for x in range(m)]
        dp[i][j] = 1
        ans = 0
        for t in range(N):
            ndp = [[0] *n for x in range(m)]
            for x in range(m):
                for y in range(n):
                    for dx, dy in dz:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            ndp[nx][ny] = (ndp[nx][ny] + dp[x][y]) % MOD
                        else:
                            ans = (ans + dp[x][y]) % MOD
            dp = ndp
        return ans



