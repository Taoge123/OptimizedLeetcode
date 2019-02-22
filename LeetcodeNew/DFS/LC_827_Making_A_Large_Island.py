
"""
For each 0, change it to a 1, then do a depth first search to find the size of that component.
The answer is the maximum size component found.

Of course, if there is no 0 in the grid, then the answer is the size of the whole grid.

"""

class Solution:
    def largestIsland(self, grid):
        N = len(grid)

        def check(r, c):
            seen = {(r, c)}
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                    if (nr, nc) not in seen and 0 <= nr < N and 0 <= nc < N and grid[nr][nc]:
                        stack.append((nr, nc))
                        seen.add((nr, nc))
            return len(seen)

        ans = 0
        has_zero = False
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 0:
                    has_zero = True
                    grid[r][c] = 1
                    ans = max(ans, check(r, c))
                    grid[r][c] = 0

        return ans if has_zero else N*N



"""
As in the previous solution, we check every 0. 
However, we also store the size of each group, 
so that we do not have to use depth-first search to repeatedly calculate the same size.

However, this idea fails when the 0 touches the same group. 
For example, consider grid = [[0,1],[1,1]]. 
The answer is 4, not 1 + 3 + 3, since the right neighbor 
and the bottom neighbor of the 0 belong to the same group.

We can remedy this problem by keeping track of a group id (or index), 
that is unique for each group. Then, 
we'll only add areas of neighboring groups with different ids.

Algorithm

For each group, fill it with value index 
and remember it's size as area[index] = dfs(...).

Then for each 0, look at the neighboring group ids seen 
and add the area of those groups, plus 1 for the 0 we are toggling. 
This gives us a candidate answer, and we take the maximum.

To solve the issue of having potentially no 0, 
we take the maximum of the previously calculated areas.
"""

class Solution1:
    def largestIsland(self, grid):
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans

        area = {}
        index = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        ans = max(area.values() or [0])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans












