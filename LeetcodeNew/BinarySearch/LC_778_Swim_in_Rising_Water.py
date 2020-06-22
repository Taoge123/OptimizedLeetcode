
"""
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].
"""
"""
思路：

一道二分查找和DFS相结合的题目，个人觉得是一道不错的面试题。通过抽茧剥丝，我们发现这道题目其实就是求从grid的左上角到右下角的所有路径中，
最大值最小的路径中的最大值（原谅我说的有点绕^_^）。

我们可以对该值进行二分查找：该值的最小可能取值就是grid中的最小值，最大可能取值就是grid中的最大值。
我们分别定义它们为left和right。然后就二分查找left和right中的合适值，使得从grid的左上角到右下角有路径可达且阈值最小。
在针对mid做一次DFS之后，可能会出现两种情况：

1）以mid为阈值无法从左上角到右下角，所以此时我们需要提高阈值，即让left = mid + 1；

2）以mid为阈值可以从左上角到右下角，所以此时我们可以降低阈值，即让right = mid - 1，以便于找到更小的阈值。

最终返回left即可。
"""

"""
这道题我本来打算用dp做，但是发现不对。比如说在12这个位置，它可能从【上、右、下】游过来，并不能靠单纯单方向的dp得到。
我的思路有点像最小生成树的prim算法。使用一个优先级队列。先压入元素0，然后pop出队首，找元素0的相邻元素，再压入队列。
每次从队列中pop出的都是当前能连通到的最小元素。一直到能连通到右下角目标元素就结束，
在这个过程中pop出的元素(即走的路径元素)中最大的那个就是result。
"""

import heapq


class SolutionTony:
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






class SolutionLeeHeap:
    def swimInWater(self, grid):
        N, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        while True:
            T, x, y = heapq.heappop(pq)
            res = max(res, T)
            if x == y == N - 1:
                return res
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
                    seen.add((i, j))
                    heapq.heappush(pq, (grid[i][j], i, j))


"""
Split this question to 2 questions:

one part of sub function reachable(int T) with T given
another part of binary search, which simply check if grid[N-1][N-1] is reachable.
"""


class SolutionLee2BinarySearch:
    def swimInWater(self, grid):
        N = len(grid)
        l, r = grid[0][0], N * N - 1

        def reachable(T):
            bfs = [(0, 0)]
            seen = set((0, 0))
            for x, y in bfs:
                if grid[x][y] <= T:
                    if x == y == N - 1:
                        return True
                    for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        if 0 <= x + i < N and 0 <= y + j < N and (x + i, y + j) not in seen:
                            seen.add((x + i, y + j))
                            bfs.append((x + i, y + j))
            return False

        while l < r:
            m = (l + r) / 2
            if reachable(m):
                r = m
            else:
                l = m + 1
        return r



class Solution1:
    def swimInWater(self, grid):
        N = len(grid)

        seen = {(0, 0)}
        pq = [(grid[0][0], 0, 0)]
        ans = 0
        while pq:
            d, r, c = heapq.heappop(pq)
            ans = max(ans, d)
            if r == c == N-1: return ans
            for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= cr < N and 0 <= cc < N and (cr, cc) not in seen:
                    heapq.heappush(pq, (grid[cr][cc], cr, cc))
                    seen.add((cr, cc))


class Solution2:
    def swimInWater(self, grid):
        N = len(grid)

        def possible(T):
            stack = [(0, 0)]
            seen = {(0, 0)}
            while stack:
                r, c = stack.pop()
                if r == c == N-1: return True
                for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if (0 <= cr < N and 0 <= cc < N
                            and (cr, cc) not in seen and grid[cr][cc] <= T):
                        stack.append((cr, cc))
                        seen.add((cr, cc))
            return False

        lo, hi = grid[0][0], N * N
        while lo < hi:
            mi = (lo + hi) / 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo

# Heap O(N^2 log N)
class Solution11:
    def swimInWater(self, grid):

        N = len(grid)
        seen = {(0, 0)}
        hp = [(grid[0][0], 0, 0)]
        ans = 0
        while hp:
            ele, r, c = heapq.heappop(hp)
            ans = max(ans, ele)
            if r == c == N-1:
                return ans
            for di in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                n_r, n_c = r + di[0], c + di[1]
                if 0 <= n_r < N and 0 <= n_c < N and (n_r, n_c) not in seen:
                    seen.add((n_r, n_c))
                    heapq.heappush(hp, (grid[n_r][n_c], n_r, n_c))


# Binary Search + DFS O(N^2 log N)
class Solution22:
    def swimInWater(self, grid):

        self.N = len(grid)
        self.grid = grid
        left, right = grid[0][0], self.N * self.N
        while left < right:
            mid = left + (right - left) // 2
            if self.check(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def check(self, ele):
        stack = [(0, 0)]
        seen = {(0, 0)}
        while stack:
            r, c = stack.pop()
            if r == c == self.N - 1:
                return True
            for di in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                n_r, n_c = r + di[0], c + di[1]
                if 0 <= n_r < self.N and 0 <= n_c < self.N and (n_r, n_c) not in seen and self.grid[n_r][n_c] <= ele:
                    seen.add((n_r, n_c))
                    stack.append((n_r, n_c))
        return False


# Union-find O(N^3)
class DSU:
    def __init__(self, N):
        self.parents = list(range(N ** 2))
        self.rank = [1] * (N ** 2)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parents[root_y] = root_x
        self.rank[root_x] += self.rank[root_y]


class Solution33:
    def swimInWater(self, grid):

        N = len(grid)
        location = {grid[i][j]: (i, j) for i in range(N) for j in range(N)}
        dsu = DSU(N)

        for t in range(N ** 2):
            r, c = location[t]
            for di in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                n_r, n_c = r + di[0], c + di[1]
                if 0 <= n_r < N and 0 <= n_c < N and grid[n_r][n_c] <= t:
                    dsu.union(r * N + c, n_r * N + n_c)
                    if dsu.find(0) == dsu.find(N ** 2 - 1):
                        return t


class UnionFind:
    def __init__(self, n):
        self.set = range(n)

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True


class Solution333:
    def swimInWater(self, grid):

        n = len(grid)
        positions = [None] * (n**2)
        for i in range(n):
            for j in range(n):
                positions[grid[i][j]] = (i, j)
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        union_find = UnionFind(n**2)
        for elevation in range(n**2):
            i, j = positions[elevation]
            for direction in directions:
                x, y = i+direction[0], j+direction[1]
                if 0 <= x < n and 0 <= y < n and grid[x][y] <= elevation:
                    union_find.union_set(i*n+j, x*n+y)
                    if union_find.find_set(0) == union_find.find_set(n**2-1):
                        return elevation
        return n**2-1


class Solution4:
    def swimInWater(self, grid):

        N = len(grid)
        ans = N * N
        lo, hi = 0, N * N - 1
        while lo <= hi:
            mi = (lo + hi) / 2
            if self.bfs(grid, mi): hi = mi - 1
            else: lo = mi + 1
        return lo

    def bfs(self, grid, limit):
        if grid[0][0] > limit: return False
        N = len(grid)
        queue = [(0, 0)]
        visits = set(queue)
        while queue:
            x, y = queue.pop(0)
            for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 \
                    or ny >= N or (nx, ny) in visits \
                    or grid[nx][ny] > limit: continue
                visits.add((nx, ny))
                queue.append((nx, ny))
        return (N - 1, N - 1) in visits

"""
思路： 
N很小，只有50，可以暴力解决。对于每一个时刻t，grid变成max(t, grid[i][j])，对grid更新后，所有<t的值都变成了t，
在这些t值上从(0， 0)dfs至(n - 1, n - 1)，如果能够找到可行的路径，输出t即可。
"""

class Solution5:
    def swimInWater(self, grid):

        N = len(grid)
        def go(i, j, mid, vis):
            if i == N - 1 and j == N - 1: return True
            vis.add((i, j))
            for d in (-1, 1):
                for ni, nj in [(i + d, j), (i, j + d)]:
                    if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in vis and max(mid, grid[i][j]) == max(mid, grid[ni][nj]):
                        if go(ni, nj, mid, vis): return True
            return False
        lf = 0
        rt = N * N
        while lf < rt:
            mid = (lf + rt) // 2
            if go(0, 0, mid, set()):
                rt = mid
            else:
                lf = mid + 1
        return rt

