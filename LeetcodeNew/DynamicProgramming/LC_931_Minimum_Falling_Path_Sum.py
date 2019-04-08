
"""
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.
The next row's choice must be in a column that is different from the previous row's column by at most one.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation:
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

Note:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
"""

"""
Let dp(r, c) be the minimum total weight of a falling path starting at (r, c) and reaching the bottom row.

Then, dp(r, c) = A[r][c] + min(dp(r+1, c-1), dp(r+1, c), dp(r+1, c+1)), and the answer is \min\limits_c \text{dp}(0, c) 
min dp(0,c)

"""
"""
Algorithm

Usually, we would make an auxillary array dp to cache intermediate values dp(r, c). 
However, this time we will use A to cache these values. Our goal is to transform the values of A into the values of dp.

We process each row, starting with the second last. (The last row is already correct.) 
We set A[r][c] = min(A[r+1][c-1], A[r+1][c], A[r+1][c+1]), handling boundary conditions gracefully.

Let's look at the recursion a little more to get a handle on why it works. 
For an array like A = [[1,1,1],[5,3,1],[2,3,4]], imagine you are at (1, 0) (A[1][0] = 5). 
You can either go to (2, 0) and get a weight of 2, or (2, 1) and get a weight of 3. 
Since 2 is lower, we say that the minimum total weight at (1, 0) is dp(1, 0) = 5 + 2 (5 for the original A[r][c].)

After visiting (1, 0), (1, 1), and (1, 2), A [which is storing the values of our dp], 
looks like [[1,1,1],[7,5,4],[2,3,4]]. We do this procedure again by visiting (0, 0), (0, 1), (0, 2). 
We get A = [[6,5,5],[7,5,4],[2,3,4]], and the final answer is min(A[0]) = 5
"""
import sys

class Solution1:
    def minFallingPathSum(self, A):
        while len(A) >= 2:
            row = A.pop()
            for i in range(len(row)):
                A[-1][i] += min(row[max(0,i-1): min(len(row), i+2)])
        return min(A[0])



class Solution2:
    def minFallingPathSum(self, A):

        dp = A[0]
        for row in A[1:]:
            dp = [value + min([dp[c], dp[max(c - 1, 0)], dp[min(len(A) - 1, c + 1)]]) for c, value in enumerate(row)]
        return min(dp)


class Solution3:
    class Solution:
        def minFallingPathSum(self, A):

            for i in range(1, len(A)):
                for j in range(len(A[0])):
                    topleft = A[i - 1][j - 1] if j - 1 >= 0 else float('inf')
                    topright = A[i - 1][j + 1] if j + 1 < len(A[0]) else float('inf')
                    A[i][j] += min(topleft, topright, A[i - 1][j])

            return min(A[-1])


"""
如果看上面这个图就明白了，数组中每个位置都要从上一层获得三个相邻列的最小值，换句话说，
每个位置都可以给下面三个相邻列传递最小值。那么，其实就是一个动态规划嘛，到每个位置的最短路径，
就是当前数值加上到达上面那层的三个相邻列的最小值。

所以这个题代码其实很简单，只需要设置好边界，然后我们每次查找上面的三个最小值加上当前的位置，得到的就是到达当前位置的最小路径。

做DP的时候，不要怕设置边界条件。我以前总想着用各种方法想着让dp数组和原来的数组一样大，这个思想是错误的！
因为我们记忆化搜索的时候实际上有很多边界条件的，其实是可以转化成dp的边界条件，或者说是初始条件。
提前给dp数组设定各种边界条件，能简化很多状态转移代码～这个题就很好的说明了这点！

时间复杂度是O(MN)，空间复杂度是O(MN)。
"""

class Solution4:
    def minFallingPathSum(self, A):

        M, N = len(A), len(A[0])
        dp = [[0] * (N + 2) for _ in range(M)]
        for i in range(M):
            dp[i][0] = dp[i][-1] = float('inf')
            for j in range(1, N + 1):
                dp[i][j] = A[i][j - 1]
        for i in range(1, M):
            for j in range(1, N + 1):
                dp[i][j] = A[i][j - 1] + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
        return min(dp[-1])



class Solution5:
    def minFallingPathSum(self, A):

        if not A: return 0
        if len(A) == 1: return A[0][0]
        length = len(A)
        for i in range(1, length):
            for j in range(0, length):
                if j == 0:
                    A[i][j] += min(A[i - 1][j], A[i - 1][j + 1])
                elif j == length - 1:
                    A[i][j] += min(A[i - 1][j - 1], A[i - 1][j])
                else:
                    A[i][j] += min(A[i - 1][j - 1], A[i - 1][j], A[i - 1][j + 1])

        return min(A[-1])

"""
define dp[i][j] means the minimum cost starts from point(i,j) to the last level
obviously, dp[i][j] = A[i][j] + min(dp[i+1][j-1],dp[i+1][j], dp[i+1][j+1])
initially, dp[n-1] = A[n-1]

题意分析：
典型的dp问题，leetcode之前有一道差不多的，那道题里面是说的树，这里是矩阵，差不多一个意思！

思路分析：
我们从下至上分析，定义dp[i][j]表示从(i,j)这个点出发，达到最底层的最小代价。
显然，我们所求的答案就是min(dp[0])。
那么有dp[i][j] = A[i][j] + min(dp[i+1][j-1],dp[i+1][j], dp[i+1][j+1])

初始化最后一行，dp[n-1] = A[n-1]！

"""
class Solution6:
    def minFallingPathSum(self, A):
        n = len(A)
        dp = [[0]*n for _ in range(n)]
        # 初始化
        for j in range(n):
            dp[n-1][j] = A[n-1][j]
        # 懒得用技巧缩短代码了，这种测试直接写才是最快的
        for i in range(n-2,-1,-1):
            for j in range(n):
                if j == 0:
                    dp[i][j] = A[i][j] + min(dp[i+1][j], dp[i+1][j+1])
                elif j == n-1:
                    dp[i][j] = A[i][j] + min(dp[i+1][j-1], dp[i+1][j])
                else:
                    dp[i][j] = A[i][j] + min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])
        return min(dp[0])


"""
Idea is simple.
Starting from row 1, for each number in the current row (A[i][j]), 
cumulate minimum previous sum from (A[i - 1][j - 1], A[i - 1][j], A[i - 1][j + 1]).
Return minimum cumulated sum in the last row
"""
class Solution7:
    def minFallingPathSum(self, A):
        for i in range(1, len(A)):
            for j in range(len(A)):
                A[i][j] += min(A[i - 1][j and j - 1:j + 2])
        return min(A[-1])

class Solution8:

    def minFallingPathSum(self, A):
        for row in A:
            row.append(sys.maxsize)
            row.insert(0, sys.maxsize)

        for i in range(1, len(A)):
            for j in range(1, len(A[0]) - 1):
                A[i][j] += min(A[i - 1][j - 1], A[i - 1][j], A[i - 1][j + 1])

        return min(A[-1])





