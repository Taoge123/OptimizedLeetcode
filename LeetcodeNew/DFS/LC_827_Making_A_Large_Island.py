
"""

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.



https://leetcode.com/problems/making-a-large-island/discuss/127032/C%2B%2BJavaPython-Straight-Forward-O(N2)-with-Explanations
https://leetcode.com/problems/making-a-large-island/discuss/210876/Python-DFS-O(N2)
https://leetcode.com/problems/making-a-large-island/discuss/234646/Python-solution-beats-100-TONS-of-comments-extremely-thorough

README
The solution is long, but in fact it is really straight forward.
I suggest not going into my codes but reading my explanations, which should be enough.

Prepare helpful subfunction:
I have several simple sub function to help me on this kind of problem.

valid(int x, int y), check if (x, y) is valid in the grid.
move(int x, int y), return all possible next position in 4 directions.
Explanation, Only 2 steps

Explore every island using DFS, count its area, give it an island index and save the result to a {index: area} map.
Loop every cell == 0, check its connected islands and calculate total islands area.
"""

class SolutionBest:
    def largestIsland(self, grid):
        N = len(grid)
        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j

        def dfs(x, y, index):
            area = 0
            grid[x][y] = index
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    area += dfs(i, j, index)
            return area + 1

        # DFS every island and give it an index of island
        index = 2
        area = {}
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    area[index] = dfs(x, y, index)
                    index += 1

        # traverse every 0 cell and count biggest island it can conntect
        res = max(area.values() or [0])
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y) if grid[i][j] > 1)
                    res = max(res, sum(area[index] for index in possible) + 1)
        return res



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










