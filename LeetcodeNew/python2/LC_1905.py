"""
https://leetcode.com/problems/count-sub-islands/discuss/1284448/easy-python-solution-on-dfs
https://leetcode.com/problems/count-sub-islands/discuss/1321673/Python-DFS-memoization
https://leetcode.com/problems/count-sub-islands/discuss/1349698/Python-DFS

"""

class SolutionDFS2:
    def countSubIslands(self, grid1, grid2):

        m, n = len(grid1), len(grid1[0])
        def dfs(i, j, visited):
            if i< 0 or i >= m or j < 0 or j >= n:
                return True

            if (i, j) in visited:
                return True
            if grid2[i][j] == 1 and grid1[i][j] == 0:
                return False
            if grid2[i][j] == 0:
                return True

            visited.add((i, j))
            res = True
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                x = i + dx
                y = j + dy
                res &= dfs(x, y, visited)

            return res

        visited = set()
        res = 0

        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue
                if grid2[i][j] == 1 and dfs(i, j, visited):
                    res += 1

        return res





