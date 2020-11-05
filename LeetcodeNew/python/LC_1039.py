

"""

https://leetcode.com/problems/minimum-score-triangulation-of-polygon/discuss/294265/Python-In-depth-Explanation-DP-For-Beginners


    1  2
 6        3
    5  4

    1-6 => 2
    []  [2 3 4 5 6]

    1-6 => 3
    [1 2 3]  [3 4 5 6]

    1-6 => 4
    [1 2 3 4]  [4 5 6]

    1-6 => 5
    [1 2 3 4 5]  []

1039.Minimum-Score-Triangulation-of-Polygon
此题是一个包装得很好的区间型DP题。

我们的突破口是，在初始状态下，两个相邻点(0,1)组成的一条边，必然有对应的一个顶点k跟它组成三角形。那么k如何选择呢？我们可以将除了(0,1)之外的点逐一尝试过来。
比如对于六边形，k可以取3，那么我们将(0,3,1)组成一个三角形后，发现将原本多边形分割为了三个区域：左边的部分(1,2,3)，中间的三角形(0,3,1)，右边的部分(3,4,5,0)。
于是显然有递归的方案：在k取3的时候，最终得到的总分就是 score(0,1,2,3,4,5) = score(1,2,3)+A[0]*A[3]*A[1]+socre(3,4,5,0)。
当然，对于其他的k的选择，我们也都需要考察一遍。答案取所有方案的最小值。

我们发现递归处理score(3,4,5,0)的时候，里面元素的index出现了wrap up，处理起来非常讨厌。这时候我们只要转换思路就可以巧妙地解决这个问题：
我们将第一步考虑的对象转换成为(0,5)这条边。继续以六边形为例，k可以取3，那么我们将(0,3,5)组成一个三角形后，发现将原本多边形分割为了三个区域：
左边的部分(0,1,2,3)，中间的三角形(0,3,5)，右边的部分(3,4,5)。我们可以发现左右两个需要递归处理的区域，里面的点的index都是连续的！

这个时候用区间型dp就可以很舒服了。dp[i][j]表示对于从i到j这些连续的点组成的多边形（当然里面包括了最后从j连回i的那条边），我们细分三角形能得到的最小的score。
显然，我们最终求的是dp[0][5]，状态转移方程就是

dp[i][j] = min{dp[i][k]+A[i][j][k]+dp[k][j]} for k=i+1,...,j-1
"""


class SolutionTD:
    def minScoreTriangulation(self, A) -> int:
        memo = {}
        return self.dfs(A, 0, len(A) - 1, memo)

    def dfs(self, nums, i, j, memo):
        # if i >= j:
        #     return 0
        if j - i + 1 < 3:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        res = float("Inf")
        for k in range(i + 1, j):
            res = min(res, nums[i] * nums[k] * nums[j] + self.dfs(nums, i, k, memo) + self.dfs(nums, k, j, memo))

        memo[(i, j)] = res
        return memo[(i, j)]




class Solution:
    def minScoreTriangulation(self, A) -> int:
        n = len(A)
        dp = [[0 for i in range(n)] for j in range(n)]

        for step in range(2, n):
            for i in range(n - step):
                j = i + step
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + A[i] * A[j] * A[k] + dp[k][j])

        return dp[0][n - 1]







