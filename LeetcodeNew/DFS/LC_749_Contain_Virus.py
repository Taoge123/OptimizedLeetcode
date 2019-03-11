
"""


Example 1:
Input: grid =
[[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]
Output: 10
Explanation:
There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left.
The board after the virus spreads is:

[[0,1,0,0,0,0,1,1],
 [0,1,0,0,0,0,1,1],
 [0,0,0,0,0,0,1,1],
 [0,0,0,0,0,0,0,1]]

On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.
Example 2:
Input: grid =
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.
Example 3:
Input: grid =
[[1,1,1,0,0,0,0,0,0],
 [1,0,1,0,1,1,1,1,1],
 [1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.


Find most threatening region (would infect most normal cells next night)
 via DFS and at same time count the walls needed to wall off,
 and return it's coordinates
Quarantine that region by doing DFS and walling that region off by setting 1's to -1's
Simulate night virus spread: find a '1' do a DFS on it and set perimeter empty spaces to 2.
Once done this for all cells, set 2's to 1. This is so that
while iterating it doesn't see newly infected cells as cells
next to the empty perimeter (then it would spread all in one night)
RT: O(MN * infected_regions)
Spc: O(MN) (could be a deep DFS)

http://www.cnblogs.com/grandyang/p/8424780.html
https://www.cnblogs.com/lightwindy/p/9582276.html


"""

import collections


class Solution1:
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(grid, r, c, lookup, regions, frontiers, perimeters):
            if (r, c) in lookup:
                return
            lookup.add((r, c))
            regions[-1].add((r, c))
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if not (0 <= nr < len(grid) and \
                        0 <= nc < len(grid[r])):
                    continue
                if grid[nr][nc] == 1:
                    dfs(grid, nr, nc, lookup, regions, frontiers, perimeters)
                elif grid[nr][nc] == 0:
                    frontiers[-1].add((nr, nc))
                    perimeters[-1] += 1

        result = 0
        while True:
            lookup, regions, frontiers, perimeters = set(), [], [], []
            for r, row in enumerate(grid):
                for c, val in enumerate(row):
                    if val == 1 and (r, c) not in lookup:
                        regions.append(set())
                        frontiers.append(set())
                        perimeters.append(0)
                        dfs(grid, r, c, lookup, regions, frontiers, perimeters)

            if not regions: break

            triage_idx = frontiers.index(max(frontiers, key=len))
            for i, region in enumerate(regions):
                if i == triage_idx:
                    result += perimeters[i]
                    for r, c in region:
                        grid[r][c] = -1
                    continue
                for r, c in region:
                    for d in directions:
                        nr, nc = r + d[0], c + d[1]
                        if not (0 <= nr < len(grid) and \
                                0 <= nc < len(grid[r])):
                            continue
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 1

        return result

class Solution:
    def containVirus(self, grid):
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def cells():
            for r in range(R):
                for c in range(C):
                    yield (r, c)

        def is_valid(i, j):
            return 0 <= i < R and 0 <= j < C

        def neighbours(r, c):
            """Get valid neighbour cells"""
            for dr, dc in dirs:
                if is_valid(r + dr, c + dc):
                    yield (r + dr, c + dc)

        def pick_most_threatening_region():
            visited = set()

            def dfs(r, c):
                """Returns number of walls needed to quarantine infected region
                starting at (r,c)"""
                # Avoid already visited or quarantined cells.
                if (r, c) in visited or grid[r][c] == -1:
                    return 0
                # Found an empty perimeter space
                if grid[r][c] == 0:
                    perimeter.add((r, c))
                    # Counts as one wall needed to contain infected cell.
                    return 1

                visited.add((r, c))
                # Explore neighbours and return the sum of the walls needed to
                # contain their perimeter.
                return sum(dfs(nr, nc) for (nr, nc) in neighbours(r, c))

            max_perimeter, max_p_walls, max_start = 0, 0, (0, 0)
            for r, c in cells():
                # Find cells that have not yet been visited and are infected.
                if (r, c) not in visited and grid[r][c] == 1:
                    perimeter = set()
                    # Get the total walls needed to quarantine the infected region.
                    walls = dfs(r, c)
                    # If the parameter we could save is the biggest we've seen...
                    if len(perimeter) > max_perimeter:
                        # update the walls needed to quarantine, and an infected cell
                        # from which we might mark the infected region as quarantined (setting -1)
                        max_perimeter, max_p_walls, max_start = len(perimeter), walls, (r, c)
            return max_p_walls, max_start

        def quarantine(r, c):
            """Mark an infected region as quarantined by setting cells to -1"""
            grid[r][c] = -1
            # Explore neighbours to quarantine them too.
            for nr, nc in neighbours(r, c):
                if grid[nr][nc] == 1:
                    quarantine(nr, nc)

        def simulate_night():
            """Spreads the infection by one night of non-quarntined regions."""

            def infected_neighbour(r, c):
                """Returns True if an orthogonally adjacent square is infected."""
                return any(grid[nr][nc] == 1 for nr, nc in neighbours(r, c))

            for r, c in cells():
                # Find clean cells that are next to infected cells
                if grid[r][c] == 0 and infected_neighbour(r, c):
                    # Set them temporarily to 2, so that further iterations do not
                    # count them as infected (otherwise it would spread endlessly
                    # in one night).
                    grid[r][c] = 2

            # Go over a second time and set the temporarily marked newly infected cells
            # to permanently infected.
            for r, c in cells():
                if grid[r][c] == 2:
                    grid[r][c] = 1

        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])

        walls = 0
        while True:
            new_walls, (r, c) = pick_most_threatening_region()
            # Stop when there are no more infected regions, i.e. only
            # -1 (quarantined by us) and 0's are left.
            if new_walls == 0:
                return walls
            quarantine(r, c)
            walls += new_walls
            simulate_night()
        return walls



class Solution2:
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        stop = False
        allCellWalls = collections.defaultdict(set)
        while not stop:
            stop = True
            quarantineNeighbors = dict()
            surroundedViruses = set()
            visitedCells = set()
            affectedCells = set()
            for x in range(m):
                for y in range(n):
                    if grid[x][y] > 0 and (x, y) not in visitedCells:
                        stop = False
                        cellWalls, virusCells = self.cellWalls(grid, x, y, m, n)
                        if not quarantineNeighbors or len(cellWalls.keys()) > len(quarantineNeighbors.keys()):
                            quarantineNeighbors = cellWalls
                            surroundedViruses = virusCells
                        affectedCells |= set(cellWalls.keys())
                        visitedCells |= virusCells
            for key in quarantineNeighbors: allCellWalls[key] |= quarantineNeighbors[key]
            confirmInfectedCells = []
            for x, y in affectedCells:
                for idx, (dx, dy) in enumerate(zip([0, -1, 0, 1], [-1, 0, 1, 0])):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] > 0 and idx not in allCellWalls[(x, y)]:
                            confirmInfectedCells.append((x, y))
                            break
            for x, y in confirmInfectedCells: grid[x][y] = 1
            for x, y in surroundedViruses: grid[x][y] = -1
        return sum(len(v) for v in allCellWalls.values())

    def cellWalls(self, grid, x, y, m, n):
        queue = [[x, y]]
        cellWalls = collections.defaultdict(set)
        virusCells = set([(x, y)])
        walls = 0
        while queue:
            px, py = queue.pop(0)
            for idx, (dx, dy) in enumerate(zip([0, 1, 0, -1], [1, 0, -1, 0])):
                nx = px + dx
                ny = py + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 0:
                        cellWalls[(nx, ny)].add(idx)
                    elif (nx, ny) not in virusCells and grid[nx][ny] > 0:
                        queue.append((nx, ny))
                        virusCells.add((nx, ny))
        return cellWalls, virusCells






