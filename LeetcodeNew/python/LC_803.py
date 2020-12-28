
"""
https://www.youtube.com/watch?v=UrMZrAyyliw

similar to 749
https://leetcode.com/problems/contain-virus/
https://leetcode.com/problems/bricks-falling-when-hit/discuss/119829/Python-Solution-by-reversely-adding-hits-bricks-back


"""


class Solution:
    def hitBricks(self, grid, hits):
        m, n = len(grid), len(grid[0])

        # Connect unconnected bricks and
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return 0
            res = 1
            grid[i][j] = 2
            res += sum(dfs(x, y) for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])
            return res

        # Check whether (i, j) is connected to Not Falling Bricks
        def is_connected(i, j):
            return i == 0 or any([0 <= x < m and 0 <= y < n and grid[x][y] == 2 for x, y in
                                  [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]])

        # Mark whether there is a brick at the each hit
        for i, j in hits:
            grid[i][j] -= 1

        # Get grid after all hits
        for i in range(n):
            dfs(0, i)

        # Reversely add the block of each hits and get count of newly add bricks
        res = [0] * len(hits)
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j] == 1 and is_connected(i, j):
                res[k] = dfs(i, j) - 1

        return res


