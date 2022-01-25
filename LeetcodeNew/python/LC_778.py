''"""
As you can swim infinite distance in zero time, the problem actually doesn't count time, but the minimum of the largest value in any path from (0,0) to (n-1,n-1).
ans = min(max(point for point in path))

Thus, we can use something like Dijkstra to expand our path by choosing the minimal reachable node. And we can use a minimal heap to acquire that minimal reachable node.

Starting from (0,0), each time we pop the smallest node from the heap and then push neighboring and unvisited nodes into the heap. Once our popped node is at (n-1,n-1),
we finished our path. Each time we update our ans as t = max(t, node's depth).

"""



import heapq

class Solution:
    def swimInWater(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        heap = []
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited = set()
        visited.add((0, 0))
        res = 0

        while heap:
            node, i, j = heapq.heappop(heap)
            res = max(res, node)

            if i == j == n - 1:
                return res

            for dx, dy in self.directions:
                x = i + dx
                y = j + dy
                if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited:
                    continue

                heapq.heappush(heap, (grid[x][y], x, y))
                visited.add((x, y))




class SolutionTony:
    def swimInWater(self, grid):
        n = len(grid)
        left, right = 0, n * n

        def dfs(i, j, limit, visited):
            if i < 0 or i >= n or j < 0 or j >= n:
                return False
            if (i, j) in visited:
                return False
            if grid[i][j] > limit:
                return False
            # Need to make sure check all false before check true
            if i == n - 1 and j == n - 1:
                return True
            visited.add((i, j))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i + dx
                y = j + dy
                # We only need one path to get true
                if dfs(x, y, limit, visited):
                    return True
            return False

        while left < right:
            mid = (left + right) // 2
            if dfs(0, 0, mid, set()):
                right = mid
            else:
                left = mid + 1
        return left





class SolutionDFS:
    def swimInWater(self, grid) -> int:
        n = len(grid)
        left = 0
        right = n * n - 1
        while left < right:
            mid = (right - left) // 2 + left
            visited = [[0 for i in range(n)] for j in range(n)]
            if self.dfs(grid, visited, 0, 0, grid[n - 1][n - 1], mid):
                right = mid
            else:
                left = mid + 1
        return left

    def dfs(self, grid, visited, i, j, target, time):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or visited[i][j] or grid[i][j] > time:
            return False
        visited[i][j] = True
        if grid[i][j] == target:
            return True
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            x = i + dx
            y = j + dy
            if self.dfs(grid, visited, x, y, target, time):
                return True
        return False




class SolutionBFS:
    def swimInWater(self, grid) -> int:
        n = len(grid)
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        left = 0
        right = n * n - 1
        while left < right:
            mid = (right - left) // 2 + left
            visited = set()
            if self.bfs(grid, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def bfs(self, grid, time):
        if grid[0][0] > time:
            return False

        queue = collections.deque()
        queue.append([0, 0])
        visited = set()
        visited.add((0, 0))

        n = len(grid)

        while queue:
            i, j = queue.popleft()

            for dx, dy in self.directions:
                x = dx + i
                y = dy + j
                if 0 <= x < n and 0 <= y < n and grid[x][y] <= time and (x, y) not in visited:
                    if x == n - 1 and y == n - 1:
                        return True
                    visited.add((x, y))
                    queue.append((x, y))

        return False
