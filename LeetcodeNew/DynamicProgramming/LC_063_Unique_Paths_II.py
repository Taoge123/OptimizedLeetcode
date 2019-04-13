
"""
https://leetcode.com/problems/unique-paths-ii/discuss/146073/Python-DP-beat-100-python-submissions
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

"""
For any other cell in the grid, we can reach it either from the cell to left of it or the cell above it.

If any cell has an obstacle, we won't let that cell contribute to any path.

We will be iterating the array from left-to-right and top-to-bottom. 
Thus, before reaching any cell we would have the number of ways of reaching the predecessor cells. 
This is what makes it a Dynamic Programming problem. 
We will be using the obstacleGrid array as the DP array thus not utilizing any additional space.

Note: As per the question, cell with an obstacle has a value 1. 
We would use this value to make sure if a cell needs to be included in the path or not. 
After that we can use the same cell to store the number of ways to reach that cell.

Algorithm

1. Rangerid[0,0] contains 1, this means there is an obstacle in the first cell. 
   Hence the robot won't be able to make any move and we would return the number of ways as 0.
2. Otherwise, if obstacleGrid[0,0] has a 0 originally we set it to 1 and move ahead.
3. Iterate the first row. If a cell originally contains a 1, this means the current cell has an obstacle and shouldn't contribute to any path. 
   Hence, set the value of that cell to 0. Otherwise, set it to the value of previous cell i.e. obstacleGrid[i,j] = obstacleGrid[i,j-1]
4. Iterate the first column. If a cell originally contains a 1, this means the current cell has an obstacle 
   and shouldn't contribute to any path. Hence, set the value of that cell to 0. 
   Otherwise, set it to the value of previous cell i.e. obstacleGrid[i,j] = obstacleGrid[i-1,j]
5. Now, iterate through the array starting from cell obstacleGrid[1,1]. 
   If a cell originally doesn't contain any obstacle then the number of ways of reaching 
   that cell would be the sum of number of ways of reaching the cell above it 
   and number of ways of reaching the cell to the left of it.

   obstacleGrid[i,j] = obstacleGrid[i-1,j] + obstacleGrid[i,j-1]

6. If a cell contains an obstacle set it to 0 and continue. This is done to make sure it doesn't contribute to any other path.
"""

class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.
        return obstacleGrid[m-1][n-1]


"""

Complexity Analysis

Time Complexity: O(M \times N)O(M×N). 
The rectangular grid given to us is of size M \times NM×N and we process each cell just once.
Space Complexity: O(1)O(1). We are utilizing the obstacleGrid as the DP array. Hence, no extra space.
"""


class SolutionCaikehe:
    # O(m*n) space
    def uniquePathsWithObstacles1(self, obstacleGrid):
        if not obstacleGrid:
            return
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, r):
            dp[i][0] = dp[i - 1][0] * (1 - obstacleGrid[i][0])
        for i in range(1, c):
            dp[0][i] = dp[0][i - 1] * (1 - obstacleGrid[0][i])
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) * (1 - obstacleGrid[i][j])
        return dp[-1][-1]

    # O(n) space
    def uniquePathsWithObstacles2(self, obstacleGrid):
        if not obstacleGrid:
            return
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        cur = [0] * c
        cur[0] = 1 - obstacleGrid[0][0]
        for i in range(1, c):
            cur[i] = cur[i - 1] * (1 - obstacleGrid[0][i])
        for i in range(1, r):
            cur[0] *= (1 - obstacleGrid[i][0])
            for j in range(1, c):
                cur[j] = (cur[j - 1] + cur[j]) * (1 - obstacleGrid[i][j])
        return cur[-1]

    # in place
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, r):
            obstacleGrid[i][0] = obstacleGrid[i - 1][0] * (1 - obstacleGrid[i][0])
        for i in range(1, c):
            obstacleGrid[0][i] = obstacleGrid[0][i - 1] * (1 - obstacleGrid[0][i])
        for i in range(1, r):
            for j in range(1, c):
                obstacleGrid[i][j] = (obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]) * (1 - obstacleGrid[i][j])
        return obstacleGrid[-1][-1]


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid):
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0] * (N - 1)
        for i in range(M):
            for j in range(N):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[N - 1]



class Solution3:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ResGrid = [[0 for x in range(n + 1)] for x in range(m + 1)]
        ResGrid[0][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not obstacleGrid[i - 1][j - 1]:
                    ResGrid[i][j] = ResGrid[i][j - 1] + ResGrid[i - 1][j]

        return ResGrid[m][n]


class Solution4:
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == rows-1 and j == cols-1:
                        dp[i][j] = 1
                    elif i == rows - 1:
                        dp[i][j] = dp[i][j+1]
                    elif j == cols -1:
                        dp[i][j] = dp[i+1][j]
                    else:
                        dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]









