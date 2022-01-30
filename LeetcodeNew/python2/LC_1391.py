
"""
https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/discuss/547229/Python-Union-Find
https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/discuss/547263/Python-easy-DFS
https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/discuss/547263/Python-easy-DFS



The center of A[0][0] has coordinates [0, 0]
The center of A[i][j] has coordinates [2i, 2j]
The top edge of A[i][j] has coordinates [2i-1, 2j]
The left edge of A[i][j] has coordinates [2i, 2j-1]
The bottom edge of A[i][j] has coordinates [2i+1, 2j]
The right edge of A[i][j] has coordinates [2i, 2j+1]

Then we apply Union Find:
if A[i][j] in [2, 5, 6]: connect center and top
if A[i][j] in [1, 3, 5]: connect center and left
if A[i][j] in [2, 3, 4]: connect center and bottom
if A[i][j] in [1, 4, 6]: connect center and right


Complexity
Time O(MN) * O(UF)
Space O(MN)

"""


import collections


class SolutionDFS:
    def hasValidPath(self, grid) -> bool:
        if not grid:
            return True

        m, n = len(grid), len(grid[0])
        directions = {1: [(0, -1), (0, 1)],
                      2: [(-1, 0), (1, 0)],
                      3: [(0, -1), (1, 0)],
                      4: [(0, 1), (1, 0)],
                      5: [(0, -1), (-1, 0)],
                      6: [(0, 1), (-1, 0)]}

        visited = set()
        goal = (m - 1, n - 1)

        def dfs(i, j):
            visited.add((i, j))
            if (i, j) == goal:
                return True
            for dx, dy in directions[grid[i][j]]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and (-dx, -dy) in directions[grid[x][y]]:
                    if dfs(x, y):
                        return True
            return False

        return dfs(0, 0)




class SolutionDFS2:
    def hasValidPath(self, grid):

        up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)

        m, n = len(grid), len(grid[0])

        directions = {1: {left: left, right: right}, 2: {up: up, down: down}, 3: {right: down, up: left},
                      4: {left: down, up: right}, 5: {right: up, down: left}, 6: {down: right, left: up}}
        visited = set()

        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return True

            visited.add((i, j))
            for dx, dy in directions[grid[i][j]].values():
                print(grid[i][j], dx, dy)
                x = i + dx
                y = j + dy
                if (x, y) in visited:
                    continue
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if (dx, dy) in directions[grid[x][y]]:
                    if dfs(x, y):
                        return True

            return False

        return dfs(0, 0)




class SolutionBFS:
    def hasValidPath(self, grid) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        queue = collections.deque([(0, 0)])
        visited[0][0] = 1
        directions = [[(0, -1), (0, 1)], [(-1, 0), (1, 0)], [(0, -1), (1, 0)], [(0, 1), (1, 0)], [(0, -1), (-1, 0)],
                      [(0, 1), (-1, 0)]]
        while queue:
            i, j = queue.popleft()
            if i == m - 1 and j == n - 1:
                return True
            for dx, dy in directions[grid[i][j] - 1]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and not visited[x][y] and (-dx, -dy) in directions[grid[x][y] - 1]:
                    visited[x][y] = 1;
                    queue.append((x, y))
        return False



class SolutionLee:
    def hasValidPath(self, A):
        m, n = len(A), len(A[0])
        parent = {(i, j): (i, j) for i in range(-1, m * 2) for j in range(-1, n * 2)}

        def find(x):
            if parent[x] == x:
                return parent[x]
            return find(parent[x])

        def merge(i, j, di, dj):
            parent[find((i, j))] = find((i + di, j + dj))

        for i in range(m):
            for j in range(n):
                if A[i][j] in [2, 5, 6]:
                    merge(i * 2, j * 2, -1, 0)
                if A[i][j] in [1, 3, 5]:
                    merge(i * 2, j * 2, 0, -1)
                if A[i][j] in [2, 3, 4]:
                    merge(i * 2, j * 2, 1, 0)
                if A[i][j] in [1, 4, 6]:
                    merge(i * 2, j * 2, 0, 1)

        return find((0, 0)) == find((m * 2 - 2, n * 2 - 2))



