
"""
In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.

Your task is to collect maximum number of cherries possible by following the rules below:


Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.


 Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation:
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.


Note:

grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
"""


class Solution1:
    def cherryPickup(self, grid):
        n = len(grid)
        if n == 0: return 0
        kMax = 2 * (n - 1)
        dp = [[-1] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for k in range(1, kMax + 1):
            cur = [[-1] * n for _ in range(n)]
            for i in range(min(n, k + 1)):
                for j in range(min(n, k + 1)):
                    if k - i >= n or k - j >= n:
                        continue
                    if grid[i][k - i] < 0 or grid[j][k - j] < 0:
                        continue

                    cherry_num = dp[i][j]
                    if i > 0:
                        cherry_num = max(cherry_num, dp[i - 1][j])
                    if j > 0:
                        cherry_num = max(cherry_num, dp[i][j - 1])
                    if i > 0 and j > 0:
                        cherry_num = max(cherry_num, dp[i - 1][j - 1])

                    if cherry_num < 0:
                        continue

                    cherry_num += grid[i][k - i] + (0 if i == j else grid[j][k - j])
                    cur[i][j] = cherry_num
            dp = cur
        return max(dp[n - 1][n - 1], 0)


"""
The idea is to use self.memo[(i1, j1, i2, j2)] to store the maximum number of cherries that can be collected 
starting from (i1, j1) to (N-1, N-1) then to(i2, j2) . 
Note that since I'm taking a step at each end at the same time, i1+j1 is always equal to i2+j2, 
therefore there are only O(N^3) states (and I'm using the full quadruple to store the state for the sake of clearness).
"""


class Solution2:
    def cherryPickup(self, grid):
        if grid[-1][-1] == -1: return 0

        # set up cache
        self.grid = grid
        self.memo = {}
        self.N = len(grid)

        return max(self.dp(0, 0, 0, 0), 0)

    def dp(self, i1, j1, i2, j2):
        # already stored: return
        if (i1, j1, i2, j2) in self.memo: return self.memo[(i1, j1, i2, j2)]

        # end states: 1. out of grid 2. at the right bottom corner 3. hit a thorn
        N = self.N
        if i1 == N or j1 == N or i2 == N or j2 == N: return -1
        if i1 == N - 1 and j1 == N - 1 and i2 == N - 1 and j2 == N - 1: return self.grid[-1][-1]
        if self.grid[i1][j1] == -1 or self.grid[i2][j2] == -1: return -1

        # now can take a step in two directions at each end, which amounts to 4 combinations in total
        dd = self.dp(i1 + 1, j1, i2 + 1, j2)
        dr = self.dp(i1 + 1, j1, i2, j2 + 1)
        rd = self.dp(i1, j1 + 1, i2 + 1, j2)
        rr = self.dp(i1, j1 + 1, i2, j2 + 1)
        maxComb = max([dd, dr, rd, rr])

        # find if there is a way to reach the end
        if maxComb == -1:
            out = -1
        else:
            # same cell, can only count this cell once
            if i1 == i2 and j1 == j2:
                out = maxComb + self.grid[i1][j1]
            # different cell, can collect both
            else:
                out = maxComb + self.grid[i1][j1] + self.grid[i2][j2]

        # cache result
        self.memo[(i1, j1, i2, j2)] = out
        return out


class Solution3:
    def cherryPickup(self, grid):

        """
        two people starting out from (0,0) picking cherries
        if their paths cross, only one cherry counted
        """

        self.cache = {}

        def pickup(r1, c1, r2, c2):

            # in cache
            if (r1, c1, r2, c2) in self.cache:
                return self.cache[(r1, c1, r2, c2)]

            n = len(grid)

            # check bounds
            if r1 == n or c1 == n or r2 == n or c2 == n:
                return float('-inf')

            # check thorn
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')

            # check if at end, return val at (n-1, n-1)
            if r1 == n - 1 and c1 == n - 1 and r2 == n - 1 and c2 == n - 1:
                return grid[-1][-1]

            rr = pickup(r1 + 1, c1, r2 + 1, c2)  # right, right
            dd = pickup(r1, c1 + 1, r2, c2 + 1)  # down, down
            rd = pickup(r1 + 1, c1, r2, c2 + 1)  # right, down
            dr = pickup(r1, c1 + 1, r2 + 1, c2)  # down, right

            best = max([rr, dd, rd, dr])

            if (r1, c1) == (r2, c2):
                # can only collect one, paths cross
                ret = best + grid[r1][c1]
            else:
                ret = best + grid[r1][c1] + grid[r2][c2]
            self.cache[(r1, c1, r2, c2)] = ret
            return ret

        return max(0, pickup(0, 0, 0, 0))


"""
Idea: Have two walkers starts from index (0,0)
Although it seems like complexity might be n^4, it is n^3, because an input must satisfy this constraight:
i1 + j1 = i2 + j2. There are only theta(n^3) such positions for a nxn grid that satisfy this.
"""
class Solution4:
    def cherryPickup(self, grid):

        dp = {}
        res = self.findMaxCherries(0, 0, 0, 0, dp, grid)
        return 0 if res == float('-inf') else res

    def findMaxCherries(self, i1, j1, i2, j2, dp, grid):
        if (i1, j1, i2, j2) in dp:
            return dp[(i1, j1, i2, j2)]
        n = len(grid)
        if i1 == n - 1 and j1 == n - 1 and i2 == n - 1 and j2 == n - 1:
            return grid[-1][-1]
        if i1 >= n or i2 >= n or j1 >= n or j2 >= n:
            return float('-inf')
        if grid[i1][j1] == -1 or grid[i2][j2] == -1:
            return float('-inf')
        best = max(
            self.findMaxCherries(i1 + 1, j1, i2 + 1, j2, dp, grid),
            self.findMaxCherries(i1 + 1, j1, i2, j2 + 1, dp, grid),
            self.findMaxCherries(i1, j1 + 1, i2 + 1, j2, dp, grid),
            self.findMaxCherries(i1, j1 + 1, i2, j2 + 1, dp, grid)
        )
        best += grid[i1][j1] if (i1, j1) == (i2, j2) else grid[i1][j1] + grid[i2][j2]
        dp[((i1, j1, i2, j2))] = best
        return best


