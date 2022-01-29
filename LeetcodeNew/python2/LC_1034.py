"""
https://www.youtube.com/watch?v=zcbFn8DH0PU
https://buptwc.com/2019/05/02/Leetcode-1034-Coloring-A-Border/
https://leetcode-cn.com/problems/coloring-a-border/solution/dfs-xun-zhao-bian-jie-bing-ran-se-by-mei-21f8/


首先理解题意：找到连通分量的边界进行着色。

连通分量：“颜色相同” 且 “相邻” 的网格块组成的整体
边界：两个判断条件：
1）在网格的边界上（网格最外围的一圈）；
2）如果不在网格边界，那么必然四个方向都有网格块，这四个网格块只要有一个与当前网格块颜色不同，那么该网格也是边界网格块
理解完题意就可以发现这就是一个简单的 dfs/bfs 题目，直接开始全文背诵（dfs版本）



"""

class SolutionDFS11:
    def colorBorder(self, grid, row, col, color):
        m, n = len(grid), len(grid[0])
        # 记录连通分量的颜色
        precolor = grid[row][col]
        visited = set()

        def dfs(i, j):
            if (i, j) in visited:
                return
            visited.add((i, j))
            # 自己在边界的时候给自己染色（边界判断条件1）
            if i in [0, m - 1] or j in [0, n - 1]:
                grid[i][j] = color

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i + dx
                y = j + dy
                if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited:
                    continue
                # 相邻存在颜色不同的块（边界判断条件2
                if grid[x][y] != precolor:
                    grid[i][j] = color
                # 颜色相同才继续 dfs，如果不在这里判断就在第一行加上另一个判断条件
                else:
                    dfs(x, y)

        dfs(row, col)
        return grid



class SolutionDFS2:
    def colorBorder(self, grid, row, col, color):
        visited = set()
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if (i, j) in visited:
                return True

            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != grid[row][col]:
                return False

            visited.add((i, j))
            count = 0
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                x = i + dx
                y = j + dy
                count += dfs(x, y)
            if count < 4:
                grid[i][j] = color
            return True

        dfs(row, col)
        return grid



class SolutionDFS1:
    def colorBorder(self, grid, r0, c0, color):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])

        self.dfs(grid, r0, c0, grid[r0][c0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    grid[i][j] = color

        return grid

    def dfs(self, grid, i, j, origin):
        grid[i][j] = -origin
        m, n = len(grid), len(grid[0])

        for node in self.directions:
            x = node[0] + i
            y = node[1] + j

            if x >= 0 and y >= 0 and x < m and y < n:
                if grid[x][y] == origin:
                    self.dfs(grid, x, y, origin)

        if i > 0 and i < m - 1 and j > 0 and j < n - 1:
            if (abs(grid[i - 1][j]) == origin and
                    abs(grid[i + 1][j]) == origin and
                    abs(grid[i][j + 1]) == origin and
                    abs(grid[i][j - 1]) == origin):
                grid[i][j] = origin

        return


class SolutionBFS:
    def colorBorder(self, grid, r0, c0, color):
        m, n = len(grid), len(grid[0])
        queue = [[r0, c0]]
        boarder = set()
        component = set([(r0, c0)])

        while queue:
            i, j = queue.pop(0)
            for node in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = i + node[0]
                y = j + node[1]
                if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == grid[r0][c0]:
                    if (x, y) not in component:
                        queue.append([x, y])
                        component.add((x, y))

                else:
                    boarder.add((i, j))

        for x, y in boarder:
            grid[x][y] = color

        return grid




class SolutionLee:
    def colorBorder(self, grid, r0, c0, color):
        m, n = len(grid), len(grid[0])
        visited = set()

        self.dfs(grid, visited, r0, c0, grid[r0][c0], color)
        return grid

    def dfs(self, grid, visited, x, y, origin, color):
        if (x, y) in visited:
            return True
        m, n = len(grid), len(grid[0])
        if not (0 <= x < m and 0 <= y < n and grid[x][y] == origin):
            return False
        visited.add((x, y))
        if self.dfs(grid, visited, x + 1, y, origin, color) + \
                self.dfs(grid, visited, x - 1, y, origin, color) + \
                self.dfs(grid, visited, x, y + 1, origin, color) + \
                self.dfs(grid, visited, x, y - 1, origin, color) < 4:
            grid[x][y] = color
        return True








