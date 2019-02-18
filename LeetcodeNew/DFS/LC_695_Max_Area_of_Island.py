


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # t: O(rc) s: O(1)
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    max_area = max(max_area, self.explore(grid, r, c))
        return max_area

    def explore(self, grid, r, c):
        if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[r])):
            return 0
        if grid[r][c] == 0:
            return 0
        # mark as visited
        grid[r][c] = 0
        return 1 + self.explore(grid, r - 1, c) + self.explore(grid, r, c - 1) + self.explore(grid, r + 1, c) + self.explore(grid, r, c + 1)



class Solution2:
    def maxAreaOfIsland(self, grid):
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) + area(r, c-1) + area(r, c+1))

        return max(area(r, c) for r in range(len(grid)) for c in range(len(grid[0])))














