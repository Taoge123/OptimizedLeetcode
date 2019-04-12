
"""
https://leetcode.com/problems/triangle/discuss/236529/python-dp
http://songhuiming.github.io/pages/2018/03/11/leetcode-120-triangle/


Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.

"""
class SolutionCaikehe:
    # O(n*n/2) space, top-down 
    def minimumTotal1(self, triangle):
        if not triangle:
            return
        res = [[0 for i in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    res[i][j] = res[i - 1][j - 1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j]
        return min(res[-1])

    # Modify the original triangle, top-down
    def minimumTotal2(self, triangle):
        if not triangle:
            return
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])

    # Modify the original triangle, bottom-up
    def minimumTotal3(self, triangle):
        if not triangle:
            return
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

    # bottom-up, O(n) space
    def minimumTotal(self, triangle):
        if not triangle:
            return
        res = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]


class Solution2:
    # O(n*n/2) space, top-down
    def minimumTotal1(self, triangle):
        l = len(triangle[-1])
        dp = [[float('inf') for _ in range(l)] for _ in range(l)]
        dp[0][0] = triangle[0][0]
        for i in range(1, l):
            for j in range(len(triangle[i])):
                val = dp[i - 1][j] if j == 0 else min(dp[i - 1][j], dp[i - 1][j - 1])
                dp[i][j] = triangle[i][j] + val
        return min(dp[-1])


class Solution3:
    def minimumTotal(self, triangle):
        f = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                f[i] = row[i] + min(f[i], f[i + 1])
        return f[0]


class Solution4:

    def minimumTotal(self, triangle):
        for i in reversed(range(len(triangle) - 1)):
            for j in range(0, i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


class Solution5:
    def minimumTotal(self, triangle):

        n = len(triangle)
        for i in range(1, n):
            for j in range(0, i + 1):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] = triangle[i][j] + min(triangle[i - 1][j - 1], triangle[i - 1][j])

        return min(triangle[n - 1])


"""
from the second layer, update the layer number every time.
from example.the following.

    [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
the first layer is 2. update the second the second layer [3+2, 4+2] = [ 5, 6]. then update the third layer
[6+5, 5+min(5, 6), 7+6] = [11, 10, 13], then the forth layer is [4+11,1+min(11, 10), 8 + min(5, 7), 3+7] = [15, 11, 13, 10], then the result is 11.
the code is like this:
"""

"""
bottom up DP

1. subproblem definition: dp(i,j) = the lowest sum to get to cell (i,j) starting from (0,0)
2. number of subproblems, |size of triangle| = number of cells in triangle
3. time per subproblem = O(1) constant (no overflow to manage)
4. recurrence dp[i][j-1] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j] )
5. total time = time per subproblem * number of subproblems = number of cells in triangle
6. top down or bottom up: bottom up
7. final answer = min(dp[last row index])

i-th row has (i+1) elements, (to allocate memory initially, 
to have the exact amount needed), probably can even "recycle" triangle to store them
"""

"""
the suggested memory improvement by problem statement,
to compute dp[rth row ] I need dp[r-1 th row], meaning all other prior dp[i] are not utilized

make a one 1-d structure that would be reutilized, 
pretty tougher to write unless Im missing something
"""
"""
(the quickest in runtime is recycling triangle (in python2 at least))
once (i,j) has been processed triangle[i][j] won't be utilized anymore, it can store
whats meant for dp[i][j] instead
recycling triangle and using it as the dp matrix
"""
"""
or even
changing the dp supproblem to

1. subproblem definition: dp(i,j) = the lowest sum to get to cell (i,j) starting any leaf
2. number of subproblems, |size of triangle| = number of cells in triangle
3. time per subproblem = O(1) constant (no overflow to manage)
4. recurrence dp[i][j-1] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1] )
5. total time = time per subproblem * number of subproblems = number of cells in triangle
6. top down or bottom up: bottom up
7. final answer = dp[0][0]
recycling triangle to store dp[i][j]
"""
class Solution6:
    def minimumTotal(self, triangle):

        m = len(triangle)
        n = len(triangle[-1])
        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp = [i for i in triangle[-1]]

        for i in range(m - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]


"""
题目大意
找出一个正三角形从顶到下的最短路径。

解题方法
很多人肯定和我一样想到的是类似于二叉树的DFS，但是二叉树的每个叶子只会遍历一遍，
但是这个三角形中，每个位置相当于被上面的两个节点所共有。所以转而用DP求解。

从顶向下的DP会导致元素越来越多，因此不是很方便，看到大神是从下向上的DP做的，很佩服！

使用minpath[k][i]保存从下向上得到的第k层第i个位置的最短路径。那么有：

minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];
1
然后可以看出minpath[k][i]只被用到了一次，所以可以变成一维DP：

For the kth level:
minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i];
1
2
代码里需要注意的是dp的初始化应该是最下面一层，然后从倒数第二层开始遍历；第layer的元素是layer + 1个。

时间复杂度为O(n^2)，空间复杂度O(n)。n为三角形高度。
"""
class Solution7:
    def minimumTotal(self, triangle):

        n = len(triangle)
        dp = triangle[-1]
        for layer in range(n - 2, -1, -1):
            for i in range(layer + 1):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[layer][i]
        return dp[0]


"""
题目大意：给定一个triangle，找出从上到下的和的最小值，每一步只能找下一行的相连的数字

解题思路：经典动态规划题。假如找到了上一层的每个点的最小值，
那么下一层的最小值可以通过上一层最小值得到。
状态：f[i][j]表示走到第i行第j列的最小值

那么我们有

转移：f[i][j]=min(f[i−1][j],f[i−1][j−1])+triangle
"""
class Solution8:
    def minimumTotal(self, triangle):
        n = len(triangle)
        # f[i][j] = min(f[i - 1][j], f[i - 1][j - 1]) + triangle
        # padding
        f = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                f[i][j] = triangle[i - 1][j - 1]
                if i == 1 and j == 1:
                    continue
                if j == 1:
                    f[i][j] += f[i - 1][j]
                elif j == i:
                    f[i][j] += f[i - 1][j - 1]
                else:
                    f[i][j] += min(f[i - 1][j], f[i - 1][j - 1])
        return min(f[n][1:])


"""
因为f[i]只跟f[i−1]有关系，所有可以使用滚动数组来压缩空间。注意要使用deepcopy。
"""

class Solution9:
    def minimumTotal(self, triangle):
        n = len(triangle)
        # padding
        # f[i][j] = min(f[i - 1][j], f[i - 1][j - 1]) + triangle
        f = [[0 for _ in range(n + 1)] for _ in range(2)]
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                f[1][j] = triangle[i - 1][j - 1]
                if i == 1 and j == 1:
                    continue
                if j == 1:
                    f[1][j] += f[0][j]
                elif j == i:
                    f[1][j] += f[0][j - 1]
                else:
                    f[1][j] += min(f[0][j], f[0][j - 1])
            f[0] = f[1][:]
        return min(f[0][1:])

"""
第三种办法，直接修改triangle，这样不需要额外的空间。因为直接修改triangle，
所以不需要padding，注意相应的i和j的起始值也要改变。
"""

class Solution10:
    def minimumTotal(self, triangle):
        n = len(triangle)
        t = triangle
        # t[i][j] = minTotalOf(i, j)
        # t[i][j] += min(t[i - 1][j], t[i - 1][j - 1])
        for i in range(0, n):
            for j in range(0, i + 1):
                if i == 0 and j == 0:
                    continue
                if j == 0:
                    t[i][j] += t[i - 1][j]
                elif j == i:
                    t[i][j] += t[i - 1][j - 1]
                else:
                    t[i][j] += min(t[i - 1][j], t[i - 1][j - 1])
        return min(t[n - 1])



