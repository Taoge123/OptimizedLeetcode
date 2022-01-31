import collections
import heapq


class SolutionDFS:
    def minimumEffortPath(self, heights):

        m, n = len(heights), len(heights[0])
        def dfs(i, j, pre, limit):
            if (i, j) in visited:
                return False
            if i < 0 or j < 0 or i >= m or j >= n or abs(heights[i][j] - pre) > limit:
                return False
            if i == m - 1 and j == n - 1:
                return True
            visited.add((i, j))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i + dx
                y = j + dy
                if dfs(x, y, heights[i][j], limit):
                    return True
            return False

        left, right = 0, 10 ** 6
        while left <= right:
            visited = set()
            mid = (left + right) // 2
            if dfs(0, 0, heights[0][0], mid):
                right = mid - 1
            else:
                left = mid + 1
        return left



class Solution:
    def minimumEffortPath(self, heights) -> int:
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        left = 0
        right = max([max(nums) for nums in heights])
        while left < right:
            mid = left + (right - left) // 2
            if self.check(heights, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def check(self, heights, num):
        m, n = len(heights), len(heights[0])
        queue = collections.deque()
        queue.append([0, 0])
        visited = [[0 for i in range(n)] for j in range(m)]
        visited[0][0] = 1

        while queue:
            i, j = queue.popleft()
            for dx, dy in self.directions:
                x = i + dx
                y = j + dy
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if visited[x][y] == 1:
                    continue
                if abs(heights[x][y] - heights[i][j]) > num:
                    continue
                queue.append([x, y])
                visited[x][y] = 1

        return visited[m - 1][n - 1] == 1





class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, i):
        if self.parent[i] == i:
            return self.parent[i]
        return self.find(self.parent[i])

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.rank[x] += 1
            self.parent[y] = x

        return True


class Solution2:
    def minimumEffortPath(self, heights) -> int:
        def convert(i, j):
            return i * n + j

        m, n = len(heights), len(heights[0])

        edges = []
        for i in range(m):
            for j in range(n):
                for dx, dy in [(1, 0), (0, 1)]:
                    x = i + dx
                    y = j + dy
                    if x < m and y < n:
                        weight = abs(heights[x][y] - heights[i][j])
                        edges.append((weight, convert(i, j), convert(x, y)))

        edges = sorted(edges)
        uf = UnionFind(m * n)

        for cost, source, dest in edges:
            uf.union(source, dest)
            if uf.find(convert(0, 0)) == uf.find(convert(m - 1, n - 1)):
                return cost
        return 0




class Solution3:
    def minimumEffortPath(self, heights) -> int:
        if not heights:
            return 0

        m, n = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        res = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        while heap:
            dist, i, j = heapq.heappop(heap)
            res = max(res, dist)
            if (i, j) == (m - 1, n - 1):
                return res

            visited.add((i, j))
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if (x, y) in visited:
                    continue
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                newDist = abs(heights[x][y] - heights[i][j])
                heapq.heappush(heap, (newDist, x, y))

        return res



heights = [[1,2,2],[3,8,2],[5,3,5]]
a = Solution3()
print(a.minimumEffortPath(heights))




