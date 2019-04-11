
"""
In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
Example 1:

Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
Example 2:

Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.
Example 3:

Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.
Note:

1. N will be an integer in the range [1, 500].
2. mines will have length at most 5000.
3. mines[i] will be length 2 and consist of integers in the range [0, N-1].
4. (Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)
"""
"""
Algorithms: For each position (i, j) of the grid matrix, we try to extend in each of the four directions (left, right, up, down) as long as possible, then take the minimum length of 1's out of the four directions as the order of the largest axis-aligned plus sign centered at position (i, j).

Optimizations: Normally we would need a total of five matrices to make the above idea work -- one matrix for the grid itself and four more matrices for each of the four directions. However, these five matrices can be combined into one using two simple tricks:

For each position (i, j), we are only concerned with the minimum length of 1's out of the four directions. This implies we may combine the four matrices into one by only keeping tracking of the minimum length.

For each position (i, j), the order of the largest axis-aligned plus sign centered at it will be 0 if and only if grid[i][j] == 0. This implies we may further combine the grid matrix with the one obtained above.

Implementations:

1. Create an N-by-N matrix grid, with all elements initialized with value N.
2. Reset those elements to 0 whose positions are in the mines list.
3. For each position (i, j), find the maximum length of 1's in each of the four directions 
   and set grid[i][j] to the minimum of these four lengths. 
   Note that there is a simple recurrence relation relating the maximum length 
   of 1's at current position with previous position for each of the four directions (labeled as l, r, u, d).
4. Loop through the grid matrix and choose the maximum element 
   which will be the largest axis-aligned plus sign of 1's contained in the grid.
"""
"""
Solutions: Here is a list of solutions for Java/C++/Python based on the above ideas. 
All solutions run at O(N^2) time with O(N^2) extra space. 
Further optimizations are possible such as keeping track of the maximum plus sign currently available 
and terminating as early as possible if no larger plus sign can be found for current row/column.

Note: For those of you who got confused by the logic within the first nested for-loop, 
refer to andier's comment below for a more clear explanation.
"""

class SolutionBruteForce:
    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        ans = 0
        for r in range(N):
            for c in range(N):
                k = 0
                while (k <= r < N-k and k <= c < N-k and
                        (r-k, c) not in banned and
                        (r+k, c) not in banned and
                        (r, c-k) not in banned and
                        (r, c+k) not in banned):
                    k += 1
                ans = max(ans, k)
        return ans

class Solution1:
    def orderOfLargestPlusSign(self, N, mines):

        grid = [[N] * N for i in range(N)]

        for m in mines:
            grid[m[0]][m[1]] = 0

        for i in range(N):
            l, r, u, d = 0, 0, 0, 0

            for j, k in zip(range(N), reversed(range(N))):
                l = l + 1 if grid[i][j] != 0 else 0
                if l < grid[i][j]:
                    grid[i][j] = l

                r = r + 1 if grid[i][k] != 0 else 0
                if r < grid[i][k]:
                    grid[i][k] = r

                u = u + 1 if grid[j][i] != 0 else 0
                if u < grid[j][i]:
                    grid[j][i] = u

                d = d + 1 if grid[k][i] != 0 else 0
                if d < grid[k][i]:
                    grid[k][i] = d

        res = 0

        for i in range(N):
            for j in range(N):
                if res < grid[i][j]:
                    res = grid[i][j]

        return res


class Solution11:
    def orderOfLargestPlusSign(self, N, mines):
        dp = [[N] * N for _ in range(N)]
        for r, c in mines:
            dp[r][c] = 0
        for i in range(N):
            l, r, t, b = 0, 0, 0, 0
            for j, k in zip(range(N), reversed(range(N))):
                l = 0 if dp[i][j] == 0 else l + 1
                dp[i][j] = min(dp[i][j], l)
                r = 0 if dp[i][k] == 0 else r + 1
                dp[i][k] = min(dp[i][k], r)
                t = 0 if dp[j][i] == 0 else t + 1
                dp[j][i] = min(dp[j][i], t)
                b = 0 if dp[k][i] == 0 else b + 1
                dp[k][i] = min(dp[k][i], b)
        return max(map(max, dp))


"""
g[x][y] is the largest plus sign allowed centered at position (x, y). 
When no mines are presented, it is only limited by the boundary and should be something similar to

1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1

Each mine would affect the row and column it is at, 
causing the value of g[x][y] to be no larger than the distance between (x, y) and the mine.
"""
class Solution2:
    def orderOfLargestPlusSign(self, N, mines):

        g = [[min(i, N-1-i, j, N-1-j) + 1 for j in range(N)] for i in range(N)]
        for (x, y) in mines:
            for i in range(N):
                g[i][y] = min(g[i][y], abs(i - x))
                g[x][i] = min(g[x][i], abs(i - y))
        return max([max(row) for row in g])


"""
解题方法
如果是暴力解法的话，我们很容易就写出O(n^3)的解法，就是对于每个位置，都向上下左右四个方向去寻找能拓展多远。
（注意，因为方向是定死的，且四个方向长度是一致的，所以不是O(n^4)）。这样肯定会超时的。

一个比较容易理解的方法就是，我们先确定一个dp数组，这个数组dp[i][j]保存的是到从i,j位置向上下左右四个方向能拓展的长度。
最后每个位置能拓展多远就是上下左右四个方向能拓展长度的最小值。
我选择遍历的方向是左右上下，那么到下的遍历的时候，dp数组保存的就就是最小的边长了。

这个题四个方向是对称的，因此只需要知道一个方向怎么写，那么直接改循环方向就行，
根本不用思考我查找的方向到底是四个方向中的哪一个。同时使用了set把二维坐标改成了一维，可以加快查找。

时间复杂度是O(n^2)，空间复杂度是O(n^2).
"""

class Solution3:
    def orderOfLargestPlusSign(self, N, mines):

        res = 0
        dp = [[0 for i in range(N)] for j in range(N)]
        s = set()
        for mine in mines:
            s.add(N * mine[0] + mine[1])
        for i in range(N):
            cnt = 0
            for j in range(N):#left
                cnt = 0 if N * i + j in s else cnt + 1
                dp[i][j] = cnt
            cnt = 0
            for j in range(N - 1, -1, -1):#right
                cnt = 0 if N * i + j in s else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
        for j in range(N):
            cnt = 0
            for i in range(N):#up
                cnt = 0 if N * i + j in s else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
            cnt = 0
            for i in range(N - 1, -1, -1):#down
                cnt = 0 if N * i + j in s else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
                res = max(dp[i][j], res)
        return res


# 如果用四个变量代表上下左右方向的话可以缩短一下代码：
class Solution33:
    def orderOfLargestPlusSign(self, N, mines):

        res = 0
        dp = [[N for i in range(N)] for j in range(N)]
        s = set()
        for mine in mines:
            dp[mine[0]][mine[1]] = 0
        for i in range(N):
            l, r, u, d = 0, 0, 0, 0
            for j in range(N):
                l = l + 1 if dp[i][j] else 0
                r = r + 1 if dp[j][i] else 0
                u = u + 1 if dp[i][N - 1 -j] else 0
                d = d + 1 if dp[N - 1 - j][i] else 0
                dp[i][j] = min(dp[i][j], l)
                dp[j][i] = min(dp[j][i], r)
                dp[i][N - 1 - j] = min(dp[i][N -  1 - j], u)
                dp[N - 1 - j][i] = min(dp[N - 1 - j][i], d)
        for i in range(N):
            for j in range(N):
                res = max(res, dp[i][j])
        return res


"""
题目大意：
二维方阵grid长宽为N，初始为全0矩阵。给定位置数组mines，在grid中将mines中的各位置设为1。

求grid中“十字形全1区域”的最大长度，关于“十字形全1区域”的定义详见测试用例。

解题思路：
时间复杂度O(N^2)

用O(N^2)的代价求出每一行的“一字型全1区域”的长度

用O(N^2)的代价求出每一列的“一字型全1区域”的长度

遍历取最小值即为“十字形全1区域”的长度
"""


class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in range(N)]
        ans = 0

        for r in range(N):
            count = 0
            for c in range(N):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count

            count = 0
            for c in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count

        for c in range(N):
            count = 0
            for r in (N):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count

            count = 0
            for r in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count
                if dp[r][c] > ans:
                    ans = dp[r][c]

        return ans



