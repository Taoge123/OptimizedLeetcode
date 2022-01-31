"""
https://leetcode-cn.com/problems/minimum-number-of-days-to-disconnect-island/solution/python-dfs-by-wzhaooooo/
https://leetcode-cn.com/problems/minimum-number-of-days-to-disconnect-island/solution/san-chong-qing-kuang-dfs-by-luosen92/


O(900) * O(900)

"""



import collections


# dfs三种情况
# 1) 全是水或岛屿个数大于1: 0天
# 2) 去除掉一个陆地后岛屿个数大于1或为0: 1天
# 3) 总能找到一个岛屿的角或是连接处将其分离: 2天

class SolutionDFS:
    def minDays(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j, visited):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x = i + dx
                y = j + dy
                if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited or grid[x][y] == 0:
                    continue
                visited.add((x, y))
                dfs(x, y, visited)

        def count(grid):
            res = 0
            visited = set()
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        # visited[i][j] = 1
                        visited.add((i, j))
                        dfs(i, j, visited)
                        res += 1
            return res

        islands = count(grid)
        if islands == 0 or islands > 1:
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # try this node see if this node is critical point, then turn it back
                    grid[i][j] = 0
                    island_num = count(grid)
                    if island_num == 0 or island_num > 1:
                        return 1
                    grid[i][j] = 1
        return 2




class SolutionWisdom:
    def minDays(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        count = self.island(grid)
        if count > 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                grid[i][j] = 0
                count = self.island(grid)
                if count > 1:
                    return 1
                grid[i][j] = 1

        return 2

    def island(self, grid):
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or (i, j) in visited:
                    continue
                queue = collections.deque()
                queue.append([i, j])
                visited.add((i, j))
                count += 1

                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        newX = x + directions[k][0]
                        newY = y + directions[k][1]

                        if newX < 0 or newX >= m or newY < 0 or newY >= n:
                            continue
                        if (newX, newY) in visited:
                            continue
                        if grid[newX][newY] == 0:
                            continue

                        queue.append([newX, newY])
                        visited.add((newX, newY))
                if count > 1:
                    return 2

        return count
